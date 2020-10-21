import insightconnect_plugin_runtime
from .schema import GetOnCallInput, GetOnCallOutput, Input, Output, Component
# Custom imports below


class GetOnCall(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_on_call',
                description=Component.DESCRIPTION,
                input=GetOnCallInput(),
                output=GetOnCallOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
