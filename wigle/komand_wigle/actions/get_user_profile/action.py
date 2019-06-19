import komand
from .schema import GetUserProfileInput, GetUserProfileOutput
# Custom imports below


class GetUserProfile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_user_profile',
                description='Get the user object for the current logged-in user',
                input=GetUserProfileInput(),
                output=GetUserProfileOutput())

    def run(self, params={}):
        self.logger.info('GetUserProfile: Fetching user profile ...')
        response = self.connection.call_api('get', 'profile/user')
        return response

    def test(self):
        return {
          "userid": "test_user",
          "email": "test@example.org",
          "donate": "?",
          "joindate": "2018-08-08T17:23:04.000Z",
          "lastlogin": "2018-08-29T14:50:30.000Z",
        }
