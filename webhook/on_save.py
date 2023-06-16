from typing import Dict, List

from sapiopylib.rest.DataMgmtService import DataMgmtServer
from sapiopylib.rest.WebhookService import AbstractWebhookHandler
from sapiopylib.rest.pojo.DataRecord import DataRecord
from sapiopylib.rest.pojo.webhook.ClientCallbackRequest import ListDialogRequest
from sapiopylib.rest.pojo.webhook.ClientCallbackResult import ListDialogResult
from sapiopylib.rest.pojo.webhook.VeloxRules import VeloxTypedRuleResult
from sapiopylib.rest.pojo.webhook.WebhookContext import SapioWebhookContext
from sapiopylib.rest.pojo.webhook.WebhookResult import SapioWebhookResult


class OnSaveWebhookHandler(AbstractWebhookHandler):
    """
    Prompts the user for the sample type if none was selected for a new sample
    """

    def run(self, context: SapioWebhookContext) -> SapioWebhookResult:
        # If we do not have a response from the user, prompt the user
        callback_result: ListDialogResult = context.client_callback_result
        if not callback_result:
            # Get the sample types in the system
            list_man = DataMgmtServer.get_picklist_manager(context.user)
            pick_list_configs = list_man.get_picklist_config_list()
            sample_types: List[str] = list()
            for config in pick_list_configs:
                if 'Exemplar Sample Types' == config.pick_list_name:
                    sample_types.extend(config.entry_list)

            if len(sample_types) == 0:
                sample_types.append('Blood')

            request = ListDialogRequest('Select a Sample Type', False, sample_types)

            return SapioWebhookResult(True, client_callback_request=request)

        # If the user cancelled, return and do nothing
        if callback_result.user_cancelled:
            return SapioWebhookResult(True)

        # Get sample type selected
        sample_type = callback_result.selected_options_list[0]

        # Set the sample type
        on_save_result_map: Dict[int, List[VeloxTypedRuleResult]] = context.velox_on_save_result_map
        samples_to_update: List[DataRecord] = list()
        for results in on_save_result_map.values():
            for result in results:
                for record in result.data_records:
                    if 'Sample' == record.get_data_type_name():
                        sample = DataRecord('Sample', record.get_record_id(), {})
                        sample.set_field_value('ExemplarSampleType', sample_type)
                        samples_to_update.append(sample)

        context.data_record_manager.commit_data_records(samples_to_update)

        return SapioWebhookResult(True)
