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
    Set sample type and container type if blank
    """

    def run(self, context: SapioWebhookContext) -> SapioWebhookResult:
        # Set the sample type
        on_save_result_map: Dict[int, List[VeloxTypedRuleResult]] = context.velox_on_save_result_map
        samples_to_update: List[DataRecord] = list()
        for results in on_save_result_map.values():
            for result in results:
                for record in result.data_records:
                    if 'Sample' == record.get_data_type_name():
                        sample = DataRecord('Sample', record.get_record_id(), {})
                        sample.set_field_value('ExemplarSampleType', 'Blood')
                        sample.set_field_value('ContainerType', 'Tube')
                        samples_to_update.append(sample)

        context.data_record_manager.commit_data_records(samples_to_update)

        return SapioWebhookResult(True)
