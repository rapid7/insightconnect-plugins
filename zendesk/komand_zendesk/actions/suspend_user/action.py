import komand
from .schema import SuspendUserInput, SuspendUserOutput
# Custom imports below
import json

class SuspendUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='suspend_user',
                description='Suspend user',
                input=SuspendUserInput(),
                output=SuspendUserOutput())

    def run(self, params={}):
        client = self.connection.client
        user = client.users(id=params.get('user_id'))
        user.suspended = "true"
        suspend = client.users.update(user)
        self.logger.debug(suspend.suspended)
        if suspend.suspended:
          return {"status": True}
        else:
          return {"status": False}

    def test(self):
        try:
          test = self.connection.client.users.me().email
          return { 'success': test }
        except:
          raise
