import insightconnect_plugin_runtime
from .schema import GetEndpointsInput, GetEndpointsOutput, Input, Output, Component
# Custom imports below


class GetEndpoints(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_endpoints',
                description=Component.DESCRIPTION,
                input=GetEndpointsInput(),
                output=GetEndpointsOutput())

    def run(self, params={}):
        return {
            Output.ITEMS: self.connection.client.get_endpoints(params.get(Input.SINCE)).get("items", [])
        }
