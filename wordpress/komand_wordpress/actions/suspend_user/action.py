import komand
from .schema import SuspendUserInput, SuspendUserOutput
# Custom imports below
import json
from komand_wordpress.util import helpers


class SuspendUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='suspend_user',
                description='Suspend user from WordPress instance',
                input=SuspendUserInput(),
                output=SuspendUserOutput())

    def run(self, params={}):
        target_user = params.get('username')
        host = self.connection.host
        username = self.connection.username
        password = self.connection.password

        creds = helpers.encode_creds(username, password)
        users = helpers.get_users(host, creds, target_user)

        if not users: raise Exception('Run: No users found')

        roles = []
        for user in users:
            if user['username'] == target_user:
                roles = user['roles']
                if not roles: 
                    self.logger.info('Run: User already has no roles')
                    return {'success': True}
                url = host + 'wp/v2/users/' + str(user['id'])
                success = helpers.post_url(url, json.dumps({'roles': []}), {'Authorization': creds, 'Accept': 'application/json', 'Content-Type': 'application/json'})         
                if not success: 
                    self.logger.error('Run: User was not suspended but API contacted')
                    break
                else:
                    self.logger.info('Run: User was suspended from roles: %s' % roles)
                    return {'success': True}
        return {'success': False}

    def test(self):
        """TODO: Test action"""
        host = self.connection.host
        username = self.connection.username
        password = self.connection.password

        creds = helpers.encode_creds(username, password)

        if not helpers.test_auth(host, creds): 
          raise Exception('Test: Failed authentication')

        return {}
