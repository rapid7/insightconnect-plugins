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
        multi_resp = {"multi_response": []}
        for i in endpoint_identifiers:
            response = client.restore_endpoint(
                pytmv1.EndpointTask(
                    endpointName=i["endpoint"], description=i.get("description", "")
                )
            )
            if "error" in response.result_code.lower():
                raise PluginException(
                    cause="An error occurred restoring endpoint.",
                    assistance="Please check the endpoint identifier and try again.",
                    data=response.errors,
                )
            else:
                multi_resp["multi_response"].append(
                    response.response.dict().get("items")[0]
                )
        # Return results
        self.logger.info("Returning Results...")
        return multi_resp
