import komand
from .schema import AddUserInput, AddUserOutput
# Custom imports below
import requests
import json


class AddUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_user',
                description='Add a user to Office365',
                input=AddUserInput(),
                output=AddUserOutput())

    def run(self, params={}):
        account_enabled = params.get('account_enabled')
        display_name = params.get('display_name')
        mail_nickname = params.get('mail_nickname')
        user_principal_name = params.get('user_principal_name')
        force_change_password = params.get('force_change_password')
        password = params.get('password')
        token = self.connection.access_token

        password_profile = {'forceChangePasswordNextSignIn': force_change_password, 'password': password}

        base_url = 'https://graph.microsoft.com/beta/users'
        headers = {'Authorization': 'Bearer %s' % token, 'Content-Type': 'application/json'}
        body = {'accountEnabled': account_enabled, 'displayName': display_name, 'mailNickname': mail_nickname,
                'userPrincipalName': user_principal_name, 'passwordProfile': password_profile}

        body = json.dumps(body)

        try:
            response = requests.post(base_url, headers=headers, data=body)
        except requests.HTTPError:
            self.logger.error('There was an issue with the add user request double check the request body:')
            self.logger.error(body)
            raise
        if response.status_code == 201:
            return {'user': response.json()}
        else:
            self.logger.error('The response from Microsoft Office indicated something went wrong: %s'
                              % response.status_code)
            self.logger.error(response.json())
            raise requests.HTTPError

    def test(self):
        if self.connection.access_token:
            return {'success': True}
        else:
            raise Exception('could not retrieve access token check your connection information')
