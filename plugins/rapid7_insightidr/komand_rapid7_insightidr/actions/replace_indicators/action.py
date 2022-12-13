import insightconnect_plugin_runtime
from .schema import ReplaceIndicatorsInput, ReplaceIndicatorsOutput, Input, Output, Component
# Custom imports below


class ReplaceIndicators(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='replace_indicators',
                description=Component.DESCRIPTION,
                input=ReplaceIndicatorsInput(),
                output=ReplaceIndicatorsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
