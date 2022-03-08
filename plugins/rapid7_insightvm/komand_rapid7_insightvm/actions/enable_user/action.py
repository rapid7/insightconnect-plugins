import insightconnect_plugin_runtime
from .schema import EnableUserInput, EnableUserOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class EnableUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="enable_user",
            description="Enable an user account",
            input=EnableUserInput(),
            output=EnableUserOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.User.users(self.connection.console_url, params.get("id"))
        self.logger.info("Using %s ..." % endpoint)

        # Get the existing details so the specific key can be modified
        payload = resource_helper.resource_request(endpoint=endpoint)

        # Delete keys not required for user update
        del payload["links"]
        del payload["role"]["name"]
        del payload["role"]["privileges"]

        # Set status
        payload["enabled"] = True
        response = resource_helper.resource_request(endpoint=endpoint, method="put", payload=payload)

        return response
