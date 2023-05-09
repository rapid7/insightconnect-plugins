import insightconnect_plugin_runtime
from .schema import DeleteUserInput, DeleteUserOutput, Input, Output, Component

# Custom imports below


class DeleteUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_user",
            description=Component.DESCRIPTION,
            input=DeleteUserInput(),
            output=DeleteUserOutput(),
        )

    def run(self, params={}):
        user_id = self.connection.api_client.get_user_id(params.get(Input.USERLOGIN))
        self.connection.api_client.delete_user(user_id, params.get(Input.SENDADMINEMAIL))

        return {
            Output.SUCCESS: True,
        }
