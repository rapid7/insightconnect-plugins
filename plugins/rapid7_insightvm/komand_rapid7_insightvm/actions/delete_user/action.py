import insightconnect_plugin_runtime
from .schema import DeleteUserInput, DeleteUserOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class DeleteUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_user",
            description="Delete an user account",
            input=DeleteUserInput(),
            output=DeleteUserOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.User.users(self.connection.console_url, params.get("id"))
        self.logger.info(f"Using {endpoint}")

        # Get the existing details so the specific role ID key can be modified
        response = resource_helper.resource_request(endpoint=endpoint, method="delete")

        return response
