import insightconnect_plugin_runtime
from .schema import (
    IsolateEndpointInput,
    IsolateEndpointOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1


class IsolateEndpoint(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="isolate_endpoint",
            description=Component.DESCRIPTION,
            input=IsolateEndpointInput(),
            output=IsolateEndpointOutput(),
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
            response = client.isolate_endpoint(
                pytmv1.EndpointTask(
                    endpointName=i["endpoint"], description=i.get("description", "")
                )
            )
            if "error" in response.result_code.lower():
                raise PluginException(
                    cause="An error occurred while isolating endpoint.",
                    assistance="Please check the endpoint name and try again.",
                    data=response.errors,
                )
            else:
                multi_resp[Output.MULTI_RESPONSE].append(
                    response.response.dict().get("items")[0]
                )
        # Return results
        self.logger.info("Returning Results...")
        return multi_resp
