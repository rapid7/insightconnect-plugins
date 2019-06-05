import komand
from .schema import DeleteUserInput, DeleteUserOutput
# Custom imports below

class DeleteUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_user',
                description='Delete specific user',
                input=DeleteUserInput(),
                output=DeleteUserOutput())

    def run(self, params={}):
        client = self.connection.box_connection
        del_user = client.user(user_id=params.get('id')).delete()
        return {"status": del_user}

    def test(self):
      try:
        client = self.connection.box_connection
        return {'status': True }
      except:
        raise
