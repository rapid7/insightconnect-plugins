import komand
from .schema import DeleteUserInput, DeleteUserOutput
# Custom imports below


class DeleteUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_user',
                description='Delete a user',
                input=DeleteUserInput(),
                output=DeleteUserOutput())

    def run(self, params={}):
        user_id = params.get('user_id')

        success = None

        try:
            self.connection.api.delete_user(user_id)
            success = True
        except Exception as e:
            self.logger.error('User deletion failed: {}'.format(e))
            success = False

        return {'success': success}

    def test(self):
        return {'success': True}
