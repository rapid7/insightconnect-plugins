import insightconnect_plugin_runtime
from .schema import EnrichIndicatorInput, EnrichIndicatorOutput, Input, Output, Component
# Custom imports below


class EnrichIndicator(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='enrich_indicator',
                description=Component.DESCRIPTION,
                input=EnrichIndicatorInput(),
                output=EnrichIndicatorOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
