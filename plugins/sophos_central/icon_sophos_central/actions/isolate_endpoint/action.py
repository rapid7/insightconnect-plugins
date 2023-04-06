import insightconnect_plugin_runtime
from .schema import IsolateEndpointInput, IsolateEndpointOutput, Output, Component

# Custom imports below
from icon_sophos_central.util.helpers import clean


class IsolateEndpoint(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="isolate_endpoint",
            description=Component.DESCRIPTION,
            input=IsolateEndpointInput(),
            output=IsolateEndpointOutput(),
        )

    def run(self, params={}):
        return {Output.ENDPOINTS: self.connection.client.isolate_endpoint(clean(params)).get("items", [])}
