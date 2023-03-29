import insightconnect_plugin_runtime
from .schema import AddEndpointToGroupInput, AddEndpointToGroupOutput, Input, Output, Component

# Custom imports below


class AddEndpointToGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_endpoint_to_group",
            description=Component.DESCRIPTION,
            input=AddEndpointToGroupInput(),
            output=AddEndpointToGroupOutput(),
        )

    def run(self, params={}):
        return {
            Output.ADDEDENDPOINTS: self.connection.client.add_endpoint_to_group(
                params.get(Input.GROUPID), {"ids": params.get(Input.IDS)}
            ).get("addedEndpoints", [])
        }
