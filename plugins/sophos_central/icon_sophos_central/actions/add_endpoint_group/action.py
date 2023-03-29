import insightconnect_plugin_runtime
from .schema import AddEndpointGroupInput, AddEndpointGroupOutput, Output, Component

# Custom imports below
from icon_sophos_central.util.helpers import clean


class AddEndpointGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_endpoint_group",
            description=Component.DESCRIPTION,
            input=AddEndpointGroupInput(),
            output=AddEndpointGroupOutput(),
        )

    def run(self, params={}):
        return {Output.ENDPOINTGROUP: self.connection.client.add_endpoint_group(clean(params))}
