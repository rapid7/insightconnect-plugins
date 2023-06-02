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
        multi_resp = {Output.MULTI_RESPONSE: []}
        for i in endpoint_identifiers:
            if i.get("endpoint_name") and i.get("agent_guid"):
                response = client.restore_endpoint(
                    pytmv1.EndpointTask(
                        endpointName=i.get("endpoint_name"),
                        agentGuid=i.get("agent_guid"),
                        description=i.get("description", ""),
                    )
                )
            elif i.get("endpoint_name") and not i.get("agent_guid"):
                response = client.restore_endpoint(
                    pytmv1.EndpointTask(
                        endpointName=i.get("endpoint_name"),
                        description=i.get("description", ""),
                    )
                )
            elif i.get("agent_guid") and not i.get("endpoint_name"):
                response = client.restore_endpoint(
                    pytmv1.EndpointTask(
                        agentGuid=i.get("agent_guid"),
                        description=i.get("description", ""),
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
            else:
                multi_resp[Output.MULTI_RESPONSE].append(
                    response.response.dict().get("items")[0]
                )
        # Return results
        self.logger.info("Returning Results...")
        return multi_resp
