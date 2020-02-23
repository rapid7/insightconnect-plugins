# Custom imports below
from komand_wordpress.util import helpers

import komand
from komand.exceptions import PluginException
from .schema import DeleteUserInput, DeleteUserOutput, Component, Input, Output


class DeleteUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='delete_user',
            description=Component.DESCRIPTION,
            input=DeleteUserInput(),
            output=DeleteUserOutput())

    def run(self, params={}):
        target_user = params.get(Input.USERNAME)
        users = helpers.get_users(self.logger, self.connection, target_user)

        if not users:
            raise PluginException(cause='Server error', assistance='Run: No users found')

        re_assign = params.get(Input.REASSIGNEE)
        r_users = helpers.get_users(self.logger, self.connection, re_assign)
        if not r_users:
            raise PluginException(cause='Server error', assistance='Run: No reassignees found')

        user_id = None
        for user in users:
            if user['username'] == target_user:
                user_id = str(user['id'])

        if not user_id:
            raise PluginException(cause='Server error', assistance='Run: No user with that username')

        re_assign_id = None
        for user in r_users:
            if user['username'] == re_assign:
                re_assign_id = str(user['id'])

        if not re_assign_id:
            raise PluginException(cause='Server error', assistance='Run: No reassignee with that username')

        success = helpers.delete_user(self.connection.host,
                                      helpers.encode_creds(self.connection.username, self.connection.password),
                                      user_id,
                                      re_assign_id)
        if not success:
            raise PluginException(cause='Server error', assistance='Run: User was not deleted')

        return {
            Output.SUCCESS: True
        }
