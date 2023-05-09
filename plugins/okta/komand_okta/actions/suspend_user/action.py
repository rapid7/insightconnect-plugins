import insightconnect_plugin_runtime
from .schema import SuspendUserInput, SuspendUserOutput, Input, Output, Component

# Custom imports below


class SuspendUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="suspend_user",
            description=Component.DESCRIPTION,
            input=SuspendUserInput(),
            output=SuspendUserOutput(),
        )

    def run(self, params={}):
        login = params.get(Input.LOGIN)
        user_id = self.connection.api_client.get_user_id(login)
        self.connection.api_client.suspend_user(user_id)

        return {
            Output.LOGIN: login,
            Output.USERID: user_id,
            Output.SUCCESS: True,
        }
