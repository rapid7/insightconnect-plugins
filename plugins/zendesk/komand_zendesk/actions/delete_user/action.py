import insightconnect_plugin_runtime
from .schema import DeleteUserInput, DeleteUserOutput, Input, Output

# Custom imports below
import json
import zenpy


class DeleteUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_user",
            description="Delete user",
            input=DeleteUserInput(),
            output=DeleteUserOutput(),
        )

    def run(self, params={}):
        try:
            user = self.connection.client.users(id=params.get(Input.USER_ID))
            self.connection.client.users.delete(user)
            return {Output.STATUS: True}
        except zenpy.lib.exception.APIException as e:
            self.logger.debug(e)
            return {Output.STATUS: False}

    def test(self):
        try:
            test = self.connection.client.users.me().email
            return {"success": test}
        except:
            raise
