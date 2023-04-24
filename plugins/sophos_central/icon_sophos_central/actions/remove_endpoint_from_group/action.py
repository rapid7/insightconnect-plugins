import insightconnect_plugin_runtime
from .schema import RemoveEndpointFromGroupInput, RemoveEndpointFromGroupOutput, Input, Output, Component

# Custom imports below


class RemoveEndpointFromGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove_endpoint_from_group",
            description=Component.DESCRIPTION,
            input=RemoveEndpointFromGroupInput(),
            output=RemoveEndpointFromGroupOutput(),
        )

    def run(self, params={}):
        response = self.connection.client.remove_endpoint_from_group(
            params.get(Input.GROUPID), {"ids": params.get(Input.IDS)}
        )
        return {
            Output.REMOVEDENDPOINTS: response.get("removedEndpoints", []),
            Output.ERRORS: response.get("errors", {}),
        }
