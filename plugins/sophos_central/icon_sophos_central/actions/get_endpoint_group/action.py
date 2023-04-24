import insightconnect_plugin_runtime
from .schema import GetEndpointGroupInput, GetEndpointGroupOutput, Input, Output, Component

# Custom imports below


class GetEndpointGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_endpoint_group",
            description=Component.DESCRIPTION,
            input=GetEndpointGroupInput(),
            output=GetEndpointGroupOutput(),
        )

    def run(self, params={}):
        return {Output.ENDPOINTGROUP: self.connection.client.get_endpoint_group(params.get(Input.GROUPID))}
