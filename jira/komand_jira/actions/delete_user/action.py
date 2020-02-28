import komand
from .schema import DeleteUserInput, DeleteUserOutput, Input, Output, Component
# Custom imports below


class DeleteUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='delete_user',
            description=Component.DESCRIPTION,
            input=DeleteUserInput(),
            output=DeleteUserOutput())

    def run(self, params={}):
        """Delete User"""
        success = self.connection.client.delete_user(
            username=params[Input.USERNAME]
        )
        return {Output.SUCCESS: success}
