import insightconnect_plugin_runtime
from .schema import GetUserByIdInput, GetUserByIdOutput
# Custom imports below
import pypd
from komand_pagerduty.util.util import empty_user, normalize_user


class GetUserById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_user_by_id',
                description='Get a User By ID',
                input=GetUserByIdInput(),
                output=GetUserByIdOutput())

    def run(self, params={}):
        """Get a user by ID"""

        if not params['id']:
            raise Exception('id required')

        user = pypd.User.find_one(id=params['id'])
        if user:
            user = normalize_user(user.json)
        else:
            user = None

        self.logger.debug('Returned: %s', user)
        return {'found': not not user, 'user': user or empty_user}

    def test(self):
        """Test action"""
        return {'found': False, 'user': empty_user}
