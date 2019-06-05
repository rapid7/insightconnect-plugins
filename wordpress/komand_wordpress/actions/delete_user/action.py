import komand
from .schema import DeleteUserInput, DeleteUserOutput
# Custom imports below
from komand_wordpress.util import helpers


class DeleteUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_user',
                description='Delete user from WordPress instance',
                input=DeleteUserInput(),
                output=DeleteUserOutput())

    def run(self, params={}):
        target_user = params.get('username')
        reassignee = params.get('reassignee')
        host = self.connection.host
        username = self.connection.username
        password = self.connection.password

        creds = helpers.encode_creds(username, password)

        users = helpers.get_users(host, creds, target_user)
        if not users: raise Exception('Run: No users found')

        r_users = helpers.get_users(host, creds, reassignee)
        if not r_users: raise Exception('Run: No reassignees found')

        user_id = None
        for user in users:
            if user['username'] == target_user:
                user_id = str(user['id']) 
        
        if not user_id: raise Exception('Run: No user with that username')

        reassignee_id = None
        for user in r_users:
            if user['username'] == reassignee:
                reassignee_id = str(user['id'])

        if not reassignee_id: raise Exception('Run: No reassignee with that username') 
        
        success = helpers.delete_user(host, creds, user_id, reassignee_id)
        if not success: raise Exception('Run: User was not deleted')
        return {'success': True}

    def test(self):
        """TODO: Test action"""
        host = self.connection.host
        username = self.connection.username
        password = self.connection.password

        creds = helpers.encode_creds(username, password)

        if not helpers.test_auth(host, creds): 
          raise Exception('Test: Failed authentication')

        return {}
