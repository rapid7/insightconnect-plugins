import insightconnect_plugin_runtime
from .schema import GetAuthenticationSourceInput, GetAuthenticationSourceOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetAuthenticationSource(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_authentication_source",
            description="Get the details for an authentication source",
            input=GetAuthenticationSourceInput(),
            output=GetAuthenticationSourceOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.AuthenticationSource.authentication_sources(self.connection.console_url, params.get("id"))
        self.logger.info("Using %s ..." % endpoint)

        response = resource_helper.resource_request(endpoint=endpoint)

        return {"authentication_source": response}
