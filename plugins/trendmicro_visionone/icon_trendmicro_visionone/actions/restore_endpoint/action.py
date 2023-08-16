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
        # Make Action API Call
        self.logger.info("Making API Call...")
        multi_resp = []
        for endpoint_identifier in endpoint_identifiers:
            if endpoint_identifier.get("endpoint_name") and endpoint_identifier.get("agent_guid"):
                response = client.restore_endpoint(
                    pytmv1.EndpointTask(
                        endpointName=endpoint_identifier.get("endpoint_name"),
                        agentGuid=endpoint_identifier.get("agent_guid"),
                        description=endpoint_identifier.get("description", ""),
                    )
                )
            elif endpoint_identifier.get("endpoint_name") and not endpoint_identifier.get("agent_guid"):
                response = client.restore_endpoint(
                    pytmv1.EndpointTask(
                        endpointName=endpoint_identifier.get("endpoint_name"),
                        description=endpoint_identifier.get("description", ""),
                    )
                )
            elif endpoint_identifier.get("agent_guid") and not endpoint_identifier.get("endpoint_name"):
                response = client.restore_endpoint(
                    pytmv1.EndpointTask(
                        agentGuid=endpoint_identifier.get("agent_guid"),
                        description=endpoint_identifier.get("description", ""),
                    )
                )
            else:
                raise PluginException(
                    cause="Neither Endpoint Name nor Agent GUID provided.",
                    assistance="Please check the provided parameters and try again.",
                )
            if "error" in response.result_code.lower():
                raise PluginException(
                    cause="An error occurred restoring endpoint.",
                    assistance="Please check the endpoint identifier and try again.",
                    data=response.errors,
                )
            multi_resp.append(response.response.dict().get("items")[0])
        # Return results
        self.logger.info("Returning Results...")
        return {Output.MULTI_RESPONSE: multi_resp}
