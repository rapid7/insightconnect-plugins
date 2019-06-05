import komand
from .schema import GetUserByEmailInput, GetUserByEmailOutput
# Custom imports below
import pypd
from komand_pagerduty.util.util import empty_user, normalize_user


class GetUserByEmail(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_user_by_email',
                description='Get a User By Email',
                input=GetUserByEmailInput(),
                output=GetUserByEmailOutput())

    def run(self, params={}):
        """Get a user by email"""

        if not params['email']:
            raise Exception('Email required')

        user = pypd.User.find_one(email=params['email'])
        if user:
            user = normalize_user(user.json)
        else:
            user = None

        self.logger.debug('Returned: %s', user)
        return {'found': bool(user), 'user': user or empty_user}

    def test(self):
        """Test action"""
        return {'found': False, 'user': empty_user}
