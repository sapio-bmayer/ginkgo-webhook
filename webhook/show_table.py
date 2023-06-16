from typing import List, Any, Dict

from sapiopylib.rest.WebhookService import AbstractWebhookHandler
from sapiopylib.rest.pojo.datatype.FieldDefinition import VeloxStringFieldDefinition
from sapiopylib.rest.pojo.eln.ExperimentEntry import ExperimentEntry
from sapiopylib.rest.pojo.webhook.ClientCallbackRequest import TableEntryDialogRequest
from sapiopylib.rest.pojo.webhook.ClientCallbackResult import TableEntryDialogResult
from sapiopylib.rest.pojo.webhook.WebhookContext import SapioWebhookContext
from sapiopylib.rest.pojo.webhook.WebhookResult import SapioWebhookResult
from sapiopylib.rest.utils.FormBuilder import FormBuilder


class ShowTableWebhookHandler(AbstractWebhookHandler):
    """
    Prompts the user with a table of data. This could come from an external source.
    """

    def run(self, context: SapioWebhookContext) -> SapioWebhookResult:
        # Get the sample entry and the records
        entries = context.eln_manager.get_experiment_entry_list(context.eln_experiment.notebook_experiment_id,
                                                                to_retrieve_field_definitions=False)
        name_to_entry: Dict[str, ExperimentEntry] = {entry.entry_name: entry for entry in entries}
        sample_entry = name_to_entry['Samples']
        samples = context.eln_manager.get_data_records_for_entry(context.eln_experiment.notebook_experiment_id,
                                                                 sample_entry.entry_id).result_list

        # If we do not have a response from the user, show the user the table
        callback_result: TableEntryDialogResult = context.client_callback_result
        if not callback_result:
            # Build what the table will look like
            form_builder: FormBuilder = FormBuilder()
            id_field = VeloxStringFieldDefinition(form_builder.get_data_type_name(), 'SampleId',
                                                  "Sample ID", max_length=2000)
            id_field.editable = False
            form_builder.add_field(id_field)
            comments_field = VeloxStringFieldDefinition(form_builder.get_data_type_name(), 'Comments',
                                                        "Comments", max_length=2000)
            comments_field.editable = False
            form_builder.add_field(comments_field)
            temp_dt = form_builder.get_temporary_data_type()

            # Build the rows of the table
            comment_index = 0
            table_data_list: List[Dict[str, Any]] = list()
            for sample in samples:
                comment_index += 1
                table_data: Dict[str, Any] = dict()
                table_data_list.append(table_data)
                table_data['SampleId'] = sample.get_field_value('SampleId')
                table_data['Comments'] = sample.get_field_value('A sample comment ' + str(comment_index))

            request = TableEntryDialogRequest('External Sample Details', '', data_type_def=temp_dt,
                                              field_map_list=table_data_list)

            return SapioWebhookResult(True, client_callback_request=request)

        # If the user cancelled, return and do nothing
        if callback_result.user_cancelled:
            return SapioWebhookResult(True)

        # Do something with the table data, if needed
        table_fields_list = callback_result.user_response_data_list
        print(table_fields_list)

        return SapioWebhookResult(True)
