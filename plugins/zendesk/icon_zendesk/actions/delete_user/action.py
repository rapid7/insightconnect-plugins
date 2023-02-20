import insightconnect_plugin_runtime
from .schema import DeleteUserInput, DeleteUserOutput, Input, Output

# Custom imports below


class DeleteUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_user",
            description="Delete user",
            input=DeleteUserInput(),
            output=DeleteUserOutput(),
        )

    def run(self, params={}):
        identifier = params.get(Input.USER_ID)

        try:
            user = self.connection.client.users(id=identifier)
            self.connection.client.users.delete(user)
            return {Output.STATUS: True}
        except Exception as error:
            self.logger.debug(error)
            return {Output.STATUS: False}
