import insightconnect_plugin_runtime
from .schema import DeleteUserInput, DeleteUserOutput, Input, Output, Component

# Custom imports below


class DeleteUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_user", description=Component.DESCRIPTION, input=DeleteUserInput(), output=DeleteUserOutput()
        )

    def run(self, params={}):
        user_id = params.get(Input.USERID)
        self.logger.info(f"Deleting user ID: {user_id}.\n")
        return {Output.SUCCESS: self.connection.client.delete_user(user_id)}
