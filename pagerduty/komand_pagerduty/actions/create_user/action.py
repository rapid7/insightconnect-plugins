import komand
from .schema import CreateUserInput, CreateUserOutput
# Custom imports below
import pypd
from komand_pagerduty.util.util import empty_user, normalize_user


class CreateUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_user',
                description='Create a User',
                input=CreateUserInput(),
                output=CreateUserOutput())

    def run(self, params={}):
        """Run action"""
        self.logger.info("Creating user %s", params)
        user = pypd.User.create(data=params, from_email=params['from_email'])

        if user:
            user = normalize_user(user.json)
        else:
            user = None

        self.logger.debug('Returned: %s', user)

        return {'success': not not user, 'user': user or empty_user}

    def test(self):
        """Test action"""

        return {'success': True, 'user': empty_user}
