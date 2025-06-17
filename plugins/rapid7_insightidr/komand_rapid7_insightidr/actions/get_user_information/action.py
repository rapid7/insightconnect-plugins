import insightconnect_plugin_runtime
from .schema import GetUserInformationInput, GetUserInformationOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Users
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper


class GetUserInformation(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user_information",
            description=Component.DESCRIPTION,
            input=GetUserInformationInput(),
            output=GetUserInformationOutput(),
        )

    def run(self, params={}):
        user_rrn = params.get(Input.USER_RRN)
        self.connection.headers["Accept-version"] = "strong-force-preview"
        request = ResourceHelper(self.connection.headers, self.logger)
        self.logger.info(f"Getting the user information for {user_rrn}...", **request.logging_context)
        response = request.make_request(Users.get_user_information(self.connection.url, user_rrn), "get")
        return {Output.USER: response, Output.SUCCESS: True}
