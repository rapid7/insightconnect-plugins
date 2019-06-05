import komand
from .schema import DeleteUserInput, DeleteUserOutput
# Custom imports below
import json
import zenpy

class DeleteUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_user',
                description='Delete user',
                input=DeleteUserInput(),
                output=DeleteUserOutput())

    def run(self, params={}):
        try:
          user = self.connection.client.users(id=params.get('user_id'))
          self.connection.client.users.delete(user)
          return {"status": True}
        except zenpy.lib.exception.APIException as e:
          self.logger.debug(e)
          return {"status": False}

    def test(self):
        try:
          test = self.connection.client.users.me().email
          return { 'success': test }
        except:
          raise