from typing import List, Dict, Any

from sapiopylib.rest.WebhookService import AbstractWebhookHandler
from sapiopylib.rest.pojo.webhook.WebhookContext import SapioWebhookContext
from sapiopylib.rest.pojo.webhook.WebhookResult import SapioWebhookResult


class PopulateListWebhookHandler(AbstractWebhookHandler):
    """
    Returns a static list of values to select from. These values could also be obtained from an external system.
    """

    def run(self, context: SapioWebhookContext) -> SapioWebhookResult:
        # Get the 'Cell Class' value from the provided context
        fields: Dict[str, Any] = context.field_map
        if not fields or 'C_Class1' not in fields.keys():
            return SapioWebhookResult(True)
        cell_class: str = fields['C_Class1']
        if not cell_class or len(cell_class) < 1:
            return SapioWebhookResult(True)

        # Determine the 'Cell Superclass' value from the provided cell class
        cell_superclasses: List[str] = list()
        if 'malignant cell' == cell_class:
            cell_superclasses.append('neoplastic cell')
        elif 'neoplastic cell' == cell_class:
            cell_superclasses.append('abnormal cell')
        elif 'fenestrated cell' == cell_class:
            cell_superclasses.append('somatic cell')
        elif 'somatic cell' == cell_class:
            cell_superclasses.append('native cell')
        elif 'primary cultured cell' == cell_class:
            cell_superclasses.append('cultured cell')
        elif 'cultured cell' == cell_class:
            cell_superclasses.append('experimentally modified cell in vitro')
        elif 'spheroplast' == cell_class:
            cell_superclasses.append('protoplast')
        elif 'protoplast' == cell_class:
            cell_superclasses.append('experimentally modified cell in vitro')
        elif 'experimentally modified cell in vitro' == cell_class:
            cell_superclasses.append('cell in vitro')
        else:
            cell_superclasses.append('cell')

        return SapioWebhookResult(True, list_values=cell_superclasses)
