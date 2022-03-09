import insightconnect_plugin_runtime
from .schema import GetUserInput, GetUserOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user",
            description="Get user account details by ID",
            input=GetUserInput(),
            output=GetUserOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.User.users(self.connection.console_url, params.get("id"))
        self.logger.info(f"Using {endpoint}")

        response = resource_helper.resource_request(endpoint)

        return {"user": response}
