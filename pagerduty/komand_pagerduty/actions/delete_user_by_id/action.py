import insightconnect_plugin_runtime
from .schema import DeleteUserByIdInput, DeleteUserByIdOutput
# Custom imports below
import pypd
from komand_pagerduty.util.util import empty_user, normalize_user


class DeleteUserById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_user_by_id',
                description='Delete a User By ID',
                input=DeleteUserByIdInput(),
                output=DeleteUserByIdOutput())

    def run(self, params={}):
        """Delete user"""

        if not params['id']:
            raise Exception('id not provided')

        user = pypd.User.find_one(id=params['id'])
        if not user:
            return {
                'success': False,
                'user': {},
            }

        self.logger.debug('Returned: %s', user)

        success = user.remove()
        user = normalize_user(user.json)

        return {'success': success, 'user': user or empty_user}

    def test(self):
        """Test action"""
        return {'success': False, 'user': empty_user}
