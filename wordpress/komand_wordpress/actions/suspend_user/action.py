# Custom imports below
import json

from komand_wordpress.util import helpers
from komand.exceptions import PluginException

import komand
from .schema import SuspendUserInput, SuspendUserOutput, Component, Input, Output


class SuspendUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='suspend_user',
            description=Component.DESCRIPTION,
            input=SuspendUserInput(),
            output=SuspendUserOutput())

    def run(self, params={}):
        target_user = params.get(Input.USERNAME)
        users = helpers.get_users(self.logger, self.connection, target_user)

        if not users:
            raise PluginException(cause='Server error', assistance='Run: No users found')

        for user in users:
            if user['username'] == target_user:
                roles = user['roles']
                if not roles:
                    self.logger.info('Run: User already has no roles')
                    return {Output.SUCCESS: True}

                url = self.connection.host + 'wp/v2/users/' + str(user['id'])
                success = helpers.post_url(url, json.dumps({'roles': []}),
                                           {'Authorization': helpers.encode_creds(self.connection.username, self.connection.password),
                                            'Accept': 'application/json',
                                            'Content-Type': 'application/json'})
                if not success:
                    self.logger.error('Run: User was not suspended but API contacted')
                    break
                else:
                    self.logger.info(f'Run: User was suspended from roles: {roles}')
                    return {Output.SUCCESS: True}

        return {Output.SUCCESS: False}
