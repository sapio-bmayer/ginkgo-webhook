from sapiopylib.rest.WebhookService import AbstractWebhookHandler
from sapiopylib.rest.pojo.eln.ElnExperiment import ElnExperimentUpdateCriteria
from sapiopylib.rest.pojo.eln.SapioELNEnums import ElnExperimentStatus
from sapiopylib.rest.pojo.webhook.ClientCallbackRequest import OptionDialogRequest
from sapiopylib.rest.pojo.webhook.ClientCallbackResult import OptionDialogResult
from sapiopylib.rest.pojo.webhook.WebhookContext import SapioWebhookContext
from sapiopylib.rest.pojo.webhook.WebhookResult import SapioWebhookResult


class LockExperimentWebhookHandler(AbstractWebhookHandler):
    """
    Prompts the user if they would like to lock the experiment. If not, it will return and do nothing
    """

    def run(self, context: SapioWebhookContext) -> SapioWebhookResult:
        # If the experiment is already locked, inform user and do nothing
        current_status = context.eln_experiment.notebook_experiment_status
        if current_status == ElnExperimentStatus.Completed:
            return SapioWebhookResult(True, display_text="The experiment is already locked.")

        # If we do not have a response from the user, prompt the user
        callback_result: OptionDialogResult = context.client_callback_result
        print(context.client_callback_result)
        print(context.client_callback_result.get_callback_type())
        if not callback_result:
            request = OptionDialogRequest('Lock Experiment?', 'Should this experiment be locked?', ['Yes', 'No'], 1,
                                          True)
            return SapioWebhookResult(True, client_callback_request=request)

        # If the user cancelled or said 'No', return and do nothing
        print(callback_result.selection)
        if callback_result.user_cancelled or callback_result.selection != 0:
            return SapioWebhookResult(True)

        # Complete the experiment
        update_criteria = ElnExperimentUpdateCriteria(new_experiment_status=ElnExperimentStatus.Completed)
        context.eln_manager.update_notebook_experiment(context.eln_experiment.notebook_experiment_id, update_criteria)

        return SapioWebhookResult(True)
