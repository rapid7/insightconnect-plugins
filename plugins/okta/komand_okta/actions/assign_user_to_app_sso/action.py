import insightconnect_plugin_runtime
from .schema import AssignUserToAppSsoInput, AssignUserToAppSsoOutput, Input, Output, Component

# Custom imports below


class AssignUserToAppSso(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="assign_user_to_app_sso",
            description=Component.DESCRIPTION,
            input=AssignUserToAppSsoInput(),
            output=AssignUserToAppSsoOutput(),
        )

    def run(self, params={}):
        response = self.connection.api_client.assign_user_to_app_sso(
            params.get(Input.APPLICATIONID), params.get(Input.APPUSER)
        )
        response["links"] = response.pop("_links")
        return {Output.RESULT: response}
