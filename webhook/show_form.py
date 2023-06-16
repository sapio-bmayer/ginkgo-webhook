from sapiopylib.rest.WebhookService import AbstractWebhookHandler
from sapiopylib.rest.pojo.datatype.FieldDefinition import VeloxStringFieldDefinition
from sapiopylib.rest.pojo.webhook.ClientCallbackRequest import FormEntryDialogRequest
from sapiopylib.rest.pojo.webhook.ClientCallbackResult import FormEntryDialogResult
from sapiopylib.rest.pojo.webhook.WebhookContext import SapioWebhookContext
from sapiopylib.rest.pojo.webhook.WebhookResult import SapioWebhookResult
from sapiopylib.rest.utils.FormBuilder import FormBuilder


class ShowFormWebhookHandler(AbstractWebhookHandler):
    """
    Prompts the user with a form of data. This could come from an external source.
    """

    def run(self, context: SapioWebhookContext) -> SapioWebhookResult:
        # Get the project ID from the context
        project = context.data_record
        project_id = project.get_field_value('ProjectId')

        # If we do not have a response from the user, show the user the form
        callback_result: FormEntryDialogResult = context.client_callback_result
        if not callback_result:
            # Build what the form will look like
            form_builder: FormBuilder = FormBuilder()
            id_field = VeloxStringFieldDefinition(form_builder.get_data_type_name(), 'ProjectId',
                                                  "Sapio ELN Project ID", max_length=2000)
            id_field.editable = False
            id_field.default_value = project_id
            form_builder.add_field(id_field)
            ginkgo_id_field = VeloxStringFieldDefinition(form_builder.get_data_type_name(), 'GinkgoId',
                                                         "Ginkgo Project ID", max_length=2000)
            ginkgo_id_field.editable = False
            ginkgo_id_field.default_value = 'Ginkgo_' + project_id
            form_builder.add_field(ginkgo_id_field)
            ginkgo_comments_field = VeloxStringFieldDefinition(form_builder.get_data_type_name(), 'GinkgoComments',
                                                               "Ginkgo Comments", max_length=2000)
            ginkgo_comments_field.editable = True
            form_builder.add_field(ginkgo_comments_field)
            temp_dt = form_builder.get_temporary_data_type()

            request = FormEntryDialogRequest('External Project Details', '', data_type_def=temp_dt)

            return SapioWebhookResult(True, client_callback_request=request)

        # If the user cancelled, return and do nothing
        if callback_result.user_cancelled:
            return SapioWebhookResult(True)

        # Do something with the data, if needed
        form_fields = callback_result.user_response_map
        print(form_fields)

        return SapioWebhookResult(True)
