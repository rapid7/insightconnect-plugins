import komand
from .schema import DeleteUserInput, DeleteUserOutput
# Custom imports below


class DeleteUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='delete_user',
            description='Delete User',
            input=DeleteUserInput(),
            output=DeleteUserOutput())

    def run(self, params={}):
        """Delete User"""
        success = self.connection.client.delete_user(
            username=params['username']
        )
        return {'success': success}
