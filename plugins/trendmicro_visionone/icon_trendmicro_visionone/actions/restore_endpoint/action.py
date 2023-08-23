import insightconnect_plugin_runtime
from .schema import (
    RestoreEndpointInput,
    RestoreEndpointOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1


class RestoreEndpoint(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="restore_endpoint",
            description=Component.DESCRIPTION,
            input=RestoreEndpointInput(),
            output=RestoreEndpointOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        endpoint_identifiers = params.get(Input.ENDPOINT_IDENTIFIERS)
        # Build endpoints list
        endpoints = []
        for endpoint in endpoint_identifiers:
            if endpoint.get("endpoint_name"):
                endpoints.append(
                    pytmv1.EndpointTask(
                        endpointName=endpoint.get("endpoint_name"),
                        description=endpoint.get("description", "Isolate Endpoint"),
                    )
                )
            elif endpoint.get("agent_guid"):
                endpoints.append(
                    pytmv1.EndpointTask(
                        agentGuid=endpoint.get("agent_guid"),
                        description=endpoint.get("description", "Isolate Endpoint"),
                    )
                )
            else:
                raise PluginException(
                    cause="Neither Endpoint Name nor Agent GUID provided.",
                    assistance="Please check the provided parameters and try again.",
                )
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.restore_endpoint(*endpoints)
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred restoring endpoint.",
                assistance="Please check the endpoint identifier and try again.",
                data=response.errors,
            )
        # Return results
        self.logger.info("Returning Results...")
        return {Output.MULTI_RESPONSE: response.response.dict().get("items")}
