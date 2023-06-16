from typing import List, Dict, Any

from sapiopylib.rest.WebhookService import AbstractWebhookHandler
from sapiopylib.rest.pojo.DataRecord import DataRecord
from sapiopylib.rest.pojo.eln.ExperimentEntryCriteria import ElnEntryCriteria
from sapiopylib.rest.pojo.eln.SapioELNEnums import ElnEntryType
from sapiopylib.rest.pojo.webhook.WebhookContext import SapioWebhookContext
from sapiopylib.rest.pojo.webhook.WebhookResult import SapioWebhookResult

from webhook.data_type_models import SampleModel


class CreateSamplesWebhookHandler(AbstractWebhookHandler):
    """
    Create a sample entry for the 'Samples' entry called 'Aliquoted Samples'
    """

    def run(self, context: SapioWebhookContext) -> SapioWebhookResult:
        # Get the sample entry and the records
        sample_entry = context.experiment_entry_list[0]
        samples = context.eln_manager.get_data_records_for_entry(context.eln_experiment.notebook_experiment_id,
                                                                 sample_entry.entry_id).result_list

        # Create a sample entry named 'Aliquoted Samples'
        criteria = ElnEntryCriteria(ElnEntryType.Table, 'Aliquoted Samples', SampleModel.DATA_TYPE_NAME,
                                    is_shown_in_template=True,
                                    order=sample_entry.order + 1,
                                    related_entry_set=[sample_entry.entry_id],
                                    notebook_experiment_tab_id=sample_entry.notebook_experiment_tab_id)
        aliquot_entry = context.eln_manager.add_experiment_entry(context.eln_experiment.notebook_experiment_id,
                                                                 entry_criteria=criteria)

        # Create a sample child for each source sample
        aliquot_samples = context.data_record_manager.add_data_records(aliquot_entry.data_type_name, len(samples))
        parent_children_map: Dict[DataRecord, List[DataRecord]] = dict()
        for source, aliquot in zip(samples, aliquot_samples):
            parent_children_map[source] = [aliquot]
        context.data_record_manager.add_children(parent_children_map)

        # Add the records to the detail entry
        context.eln_manager.add_records_to_table_entry(context.eln_experiment.notebook_experiment_id,
                                                       aliquot_entry.entry_id, aliquot_samples)

        return SapioWebhookResult(True)
