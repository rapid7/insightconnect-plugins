import insightconnect_plugin_runtime
from .schema import GetEndpointDetailsInput, GetEndpointDetailsOutput, Input, Output, Component

# Custom imports below


class GetEndpointDetails(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_endpoint_details",
            description=Component.DESCRIPTION,
            input=GetEndpointDetailsInput(),
            output=GetEndpointDetailsOutput(),
        )

    def run(self, params={}):
        endpoint = params.get(Input.ENDPOINT)
        self.logger.info(f"Searching for: {endpoint}")
        output = insightconnect_plugin_runtime.helper.clean(self.connection.xdr_api.get_endpoint_information(endpoint))
        self.logger.info("Get Endpoint Details complete.")
        return output
