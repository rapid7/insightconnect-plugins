import komand
from .schema import SuspendUserInput, SuspendUserOutput
# Custom imports below


class SuspendUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='suspend_user',
                description='Suspend a User',
                input=SuspendUserInput(),
                output=SuspendUserOutput())

    def run(self, params={}):
        body = {'suspended': True}
        user = self.connection.service.users().update(userKey=params['user'], body=body).execute()
        return {'user': user}

    def test(self):
        # TODO: Implement test function
        return {}
