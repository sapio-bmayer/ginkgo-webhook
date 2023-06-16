from typing import List

from sapiopylib.rest.WebhookService import AbstractWebhookHandler
from sapiopylib.rest.pojo.webhook.WebhookContext import SapioWebhookContext
from sapiopylib.rest.pojo.webhook.WebhookResult import SapioWebhookResult


class PopulateListWebhookHandler(AbstractWebhookHandler):
    """
    Returns a static list of values to select from. These values could also be obtained from an external system.
    """

    def run(self, context: SapioWebhookContext) -> SapioWebhookResult:
        ginkgo_materials: List[str] = list()
        ginkgo_materials.append('OZ-AI20100')
        ginkgo_materials.append('OZ-AI20250')
        ginkgo_materials.append('OZ-AI20500')
        ginkgo_materials.append('OZ-AI21000')
        ginkgo_materials.append('OZ-AI20050')
        ginkgo_materials.append('NM_182961')
        ginkgo_materials.append('FuGENE® 4K Transfection Reagent')
        ginkgo_materials.append('80% Ethanol')
        ginkgo_materials.append('10XNSPI')
        ginkgo_materials.append('BDH20880.100E')

        return SapioWebhookResult(True, list_values=ginkgo_materials)
