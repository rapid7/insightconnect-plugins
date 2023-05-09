import insightconnect_plugin_runtime
from .schema import GetUserInput, GetUserOutput, Input, Output, Component

# Custom imports below
from komand_okta.util.helpers import clean


class GetUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user",
            description=Component.DESCRIPTION,
            input=GetUserInput(),
            output=GetUserOutput(),
        )

    def run(self, params={}):
        login = params.get(Input.LOGIN)
        response = self.connection.api_client.get_user(login)
        response["links"] = response.pop("_links")
        if response.get("credentials") and response["credentials"].get("recovery_question"):
            response["credentials"]["recoveryQuestion"] = response["credentials"].pop("recovery_question")
        return {
            Output.USER: clean(response),
        }
