from typing import List, Dict, Any

from sapiopylib.rest.WebhookService import AbstractWebhookHandler
from sapiopylib.rest.pojo.eln.ExperimentEntryCriteria import ElnEntryCriteria
from sapiopylib.rest.pojo.eln.SapioELNEnums import ElnEntryType, ElnBaseDataType
from sapiopylib.rest.pojo.webhook.WebhookContext import SapioWebhookContext
from sapiopylib.rest.pojo.webhook.WebhookResult import SapioWebhookResult


class CreateDetailsWebhookHandler(AbstractWebhookHandler):
    """
    Create a sample detail entry for the 'Samples' entry and populate the Ginkgo Material field
    """

    def run(self, context: SapioWebhookContext) -> SapioWebhookResult:
        # Get the sample entry and the records
        sample_entry = context.experiment_entry_list[0]
        samples = context.eln_manager.get_data_records_for_entry(context.eln_experiment.notebook_experiment_id,
                                                                 sample_entry.entry_id).result_list
        print(samples)

        # Get the Ginkgo Material and Amount fields
        ginkgo_amount_field = context.eln_manager.get_predefined_field_by_name(ElnBaseDataType.SAMPLE_DETAIL,
                                                                               'GinkgoAmount')
        ginkgo_material_field = context.eln_manager.get_predefined_field_by_name(ElnBaseDataType.SAMPLE_DETAIL,
                                                                                 'GinkgoMaterial')

        # Create a sample detail entry named 'Ginkgo Details'
        criteria = ElnEntryCriteria(ElnEntryType.Table, 'Ginkgo Details', ElnBaseDataType.SAMPLE_DETAIL.data_type_name,
                                    is_shown_in_template=True,
                                    order=sample_entry.order + 1,
                                    related_entry_set=[sample_entry.entry_id],
                                    notebook_experiment_tab_id=sample_entry.notebook_experiment_tab_id,
                                    field_definition_list=[ginkgo_material_field, ginkgo_amount_field])
        detail_entry = context.eln_manager.add_experiment_entry(context.eln_experiment.notebook_experiment_id,
                                                                entry_criteria=criteria)

        # Create a detail record for each sample populating the relevant fields
        detail_fields_list: List[Dict[str, Any]] = list()
        for sample in samples:
            detail_fields: Dict[str, Any] = dict()
            detail_fields_list.append(detail_fields)
            detail_fields['SampleId'] = sample.get_field_value('SampleId')
            detail_fields['OtherSampleId'] = sample.get_field_value('OtherSampleId')
            detail_fields['GinkgoMaterial'] = sample.get_field_value('C_GinkgoMaterial')
        print(detail_fields_list)

        detail_records = context.data_record_manager.add_data_records_with_data(detail_entry.data_type_name,
                                                                                detail_fields_list)

        # Add the records to the detail entry
        context.eln_manager.add_records_to_table_entry(context.eln_experiment.notebook_experiment_id,
                                                       detail_entry.entry_id, detail_records)

        return SapioWebhookResult(True)
