from typing import Dict, Any, List

from sapiopylib.rest.WebhookService import AbstractWebhookHandler
from sapiopylib.rest.pojo.datatype.FieldDefinition import VeloxStringFieldDefinition, VeloxEnumFieldDefinition
from sapiopylib.rest.pojo.webhook.ClientCallbackRequest import FormEntryDialogRequest
from sapiopylib.rest.pojo.webhook.ClientCallbackResult import FormEntryDialogResult
from sapiopylib.rest.pojo.webhook.WebhookContext import SapioWebhookContext
from sapiopylib.rest.pojo.webhook.WebhookResult import SapioWebhookResult
from sapiopylib.rest.utils.FormBuilder import FormBuilder
from slack import WebClient

api_key_field: str = 'Slack Token'
user_field: str = 'User To Review Experiment'


def prompt_api_key() -> SapioWebhookResult:
    form_builder: FormBuilder = FormBuilder()
    key_field = VeloxStringFieldDefinition(form_builder.get_data_type_name(), api_key_field,
                                           api_key_field, max_length=200)
    key_field.editable = True
    key_field.required = True
    form_builder.add_field(key_field)

    temp_dt = form_builder.get_temporary_data_type()
    request = FormEntryDialogRequest('Slack Integration',
                                     'Please enter the slack token to use to integrate with slack.',
                                     data_type_def=temp_dt)

    return SapioWebhookResult(True, client_callback_request=request)


def prompt_for_user(token: str, values: List[str]) -> SapioWebhookResult:
    form_builder: FormBuilder = FormBuilder()
    key_field = VeloxStringFieldDefinition(form_builder.get_data_type_name(), api_key_field,
                                           api_key_field, max_length=200, default_value=token)
    key_field.visible = False
    form_builder.add_field(key_field)

    user_def = VeloxEnumFieldDefinition(form_builder.get_data_type_name(), user_field,
                                        user_field, default_value=0, values=values)
    user_def.editable = True
    user_def.required = True
    form_builder.add_field(user_def)

    temp_dt = form_builder.get_temporary_data_type()
    request = FormEntryDialogRequest('Slack Integration',
                                     'Please select a user to review your experiment.',
                                     data_type_def=temp_dt)

    return SapioWebhookResult(True, client_callback_request=request)


def get_slack_users(token: str) -> Dict[str, str]:
    username_to_id: Dict[str, str] = dict()

    client: WebClient = WebClient(token=token)

    try:
        # Call the `users.list` API method to retrieve the user list
        response = client.users_list()
        if response["ok"]:
            users = response["members"]
            for user in users:
                if 'deleted' in user and user['deleted']:
                    continue
                if 'is_bot' in user and user['is_bot']:
                    continue

                user_id = user["id"]
                user_name: str
                if 'profile' in user:
                    profile = user['profile']
                    if 'first_name' in profile and 'last_name' in profile:
                        user_name = profile['first_name'] + ' ' + profile['last_name']
                    elif 'real_name' in profile:
                        user_name = profile['real_name']
                    else:
                        user_name = user['name']
                else:
                    user_name = user['name']
                username_to_id[user_name] = user_id
        else:
            print(f"Error: {response['error']}")
    except Exception as e:
        print(f"Error: {str(e)}")

    return username_to_id


def send_slack_message(token: str, channel: str, experiment_name: str, experiment_url: str):
    client: WebClient = WebClient(token=token)

    try:
        message_response = client.chat_postMessage(
            channel=channel,
            text='Please Review My Experiment: <' + experiment_url + '|' + experiment_name + '>'
        )
        if message_response["ok"]:
            print(f"Direct message sent to user: {channel}")
        else:
            print(f"Error sending direct message to user: {channel}. Error: {message_response['error']}")
    except Exception as e:
        print(f"Error: {str(e)}")


class SlackIntegration(AbstractWebhookHandler):
    """
    Example of integrating with slack
    """

    def run(self, context: SapioWebhookContext) -> SapioWebhookResult:
        callback_result: FormEntryDialogResult = context.client_callback_result
        if not callback_result:
            # Get API key first
            return prompt_api_key()
        elif callback_result.user_cancelled:
            # User cancelled
            return SapioWebhookResult(True)

        # Get API key
        response_map: Dict[str, Any] = callback_result.user_response_map
        if not response_map or api_key_field not in response_map.keys():
            return SapioWebhookResult(True)
        api_key: str = response_map[api_key_field]

        # Get users to send message to
        name_to_id = get_slack_users(api_key)
        if user_field not in response_map.keys():
            return prompt_for_user(api_key, list(name_to_id.keys()))
        user: int = response_map[user_field]

        # Send chat message
        user_id: str = list(name_to_id.keys())[user]
        experiment: str = context.eln_experiment.notebook_experiment_name
        url: str = "https://ginkgo.exemplareln.com/veloxClient/#notebookExperimentId=" + \
                   str(context.eln_experiment.notebook_experiment_id) + ";view=eln"
        send_slack_message(api_key, user_id, experiment, url)

        return SapioWebhookResult(True)
