import komand
from .schema import GetUserInput, GetUserOutput
# Custom imports below


class GetUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_user',
                description='Get a User',
                input=GetUserInput(),
                output=GetUserOutput())

    def run(self, params={}):
        user = self.connection.service.users().get(userKey=params['user']).execute()
        return {'user': user, 'found': (not not user)}

    def test(self):
        # TODO: Implement test function
        return {}
