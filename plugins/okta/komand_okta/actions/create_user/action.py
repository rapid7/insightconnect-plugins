import insightconnect_plugin_runtime
from .schema import CreateUserInput, CreateUserOutput, Input, Component, Output

# Custom imports below
from komand_okta.util.helpers import clean


class CreateUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_user",
            description=Component.DESCRIPTION,
            input=CreateUserInput(),
            output=CreateUserOutput(),
        )

    def run(self, params={}):  # noqa: MC0001
        json_params = {
            "profile": params.get(Input.PROFILE, {}),
            "credentials": params.get(Input.CREDENTIALS, {}),
            "groupIds": params.get(Input.GROUPIDS, []),
        }

        credentials = json_params.get("credentials", False)

        if credentials.get("recoveryQuestion"):
            credentials["recovery_question"] = credentials.pop("recoveryQuestion")
            json_params["credentials"] = credentials

        url_params = {
            "activate": str(params.get(Input.ACTIVATE, True)).lower(),
            "provider": str(params.get(Input.PROVIDER, False)).lower(),
            "nextLogin": "changePassword" if params.get(Input.NEXTLOGIN) else "false",
        }

        response = self.connection.api_client.create_user(clean(url_params), clean(json_params))
        response["links"] = response.pop("_links")

        response_credentials = response.get("credentials", False)
        if response_credentials.get("recovery_question"):
            response_credentials["recoveryQuestion"] = response_credentials.pop("recovery_question")
            response["credentials"] = response_credentials

        return {Output.USER: response}
