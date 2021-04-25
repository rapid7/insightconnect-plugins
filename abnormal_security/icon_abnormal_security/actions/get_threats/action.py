import insightconnect_plugin_runtime
from .schema import GetThreatsInput, GetThreatsOutput, Input, Output, Component
# Custom imports below


class GetThreats(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_threats',
                description=Component.DESCRIPTION,
                input=GetThreatsInput(),
                output=GetThreatsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
