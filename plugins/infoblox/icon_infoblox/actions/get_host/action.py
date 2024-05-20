import insightconnect_plugin_runtime
from .schema import GetHostInput, GetHostOutput, Input, Output, Component

# Custom imports below


class GetHost(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_host",
            description=Component.DESCRIPTION,
            input=GetHostInput(),
            output=GetHostOutput(),
        )

    def run(self, params={}):
        ref = params.get(Input.REF)

        return {Output.HOST: self.connection.infoblox_connection.get_host(ref)}
