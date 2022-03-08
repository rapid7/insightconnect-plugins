import insightconnect_plugin_runtime
from .schema import GetAuthenticationSourcesInput, GetAuthenticationSourcesOutput

# Custom imports below
import re
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetAuthenticationSources(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_authentication_sources",
            description="List authentication sources available for InsightVM users",
            input=GetAuthenticationSourcesInput(),
            output=GetAuthenticationSourcesOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.AuthenticationSource.authentication_sources(self.connection.console_url)
        self.logger.info("Using %s ..." % endpoint)

        response = resource_helper.resource_request(endpoint)["resources"]

        # Filter response
        name = params.get("name")
        if name and (name != ""):
            name_regex = re.compile(name, re.IGNORECASE)
            response = [r for r in response if name_regex.match(r["name"])]
            self.logger.info(f"Returning {len(response)} results based on filter...")

        return {"authentication_sources": response}
