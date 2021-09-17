import insightconnect_plugin_runtime
from .schema import RescanIndicatorInput, RescanIndicatorOutput, Input, Output, Component
# Custom imports below


class RescanIndicator(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='rescan_indicator',
                description=Component.DESCRIPTION,
                input=RescanIndicatorInput(),
                output=RescanIndicatorOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
