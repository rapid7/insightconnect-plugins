import insightconnect_plugin_runtime
from .schema import GetThreatDetailsInput, GetThreatDetailsOutput, Input, Output, Component
# Custom imports below


class GetThreatDetails(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_threat_details',
                description=Component.DESCRIPTION,
                input=GetThreatDetailsInput(),
                output=GetThreatDetailsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
