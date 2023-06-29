from typing import List, Dict, Any

from sapiopylib.rest.WebhookService import AbstractWebhookHandler
from sapiopylib.rest.pojo.DataRecord import DataRecord
from sapiopylib.rest.pojo.eln.ExperimentEntry import ExperimentEntry
from sapiopylib.rest.pojo.webhook.WebhookContext import SapioWebhookContext
from sapiopylib.rest.pojo.webhook.WebhookResult import SapioWebhookResult

from webhook.data_type_models import SampleModel


class SetFieldsWebhookHandler(AbstractWebhookHandler):
    """
    On submit of a sample entry, update some fields on the sample records for that entry.
    """

    def run(self, context: SapioWebhookContext) -> SapioWebhookResult:
        # Get the sample entry and the samples
        sample_entry: ExperimentEntry = context.experiment_entry_list[0]
        samples: List[DataRecord] = context.eln_manager.get_data_records_for_entry(context.eln_experiment
                                                                                   .notebook_experiment_id,
                                                                                   sample_entry.entry_id).result_list

        # Update the volume and concentration fields for the samples. These could come from an external system
        samples_to_update: List[DataRecord] = list()
        for idx, sample in enumerate(samples):
            sample_fields: Dict[str, Any] = dict()
            sample_fields[SampleModel.VOLUME__FIELD_NAME.field_name] = (idx + 1) * 10.2
            sample_fields[SampleModel.VOLUMEUNITS__FIELD_NAME.field_name] = 'mL'
            sample_fields[SampleModel.CONCENTRATION__FIELD_NAME.field_name] = (idx + 2) * 7.8
            sample_fields[SampleModel.CONCENTRATIONUNITS__FIELD_NAME.field_name] = 'ng/mL'

            # We need to recreate the DataRecord object for each sample, so we only update the exact fields
            sample_to_update: DataRecord = DataRecord(SampleModel.DATA_TYPE_NAME, sample.get_record_id(), dict())
            sample_to_update.set_fields(sample_fields)
            samples_to_update.append(sample_to_update)

        # Store the changes and return. The values will automatically refresh within the client
        context.data_record_manager.commit_data_records(samples_to_update)

        return SapioWebhookResult(True)
