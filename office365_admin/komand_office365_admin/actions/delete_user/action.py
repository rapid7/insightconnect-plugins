import komand
from .schema import DeleteUserInput, DeleteUserOutput
# Custom imports below
import requests


class DeleteUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_user',
                description='Remove a user\'s access to Office365',
                input=DeleteUserInput(),
                output=DeleteUserOutput())

    def run(self, params={}):
        user_principal_name = params.get('user_principal_name')
        token = self.connection.access_token

        base_url = 'https://graph.microsoft.com/beta/users/%s' % user_principal_name
        headers = {'Authorization': 'Bearer %s' % token}

        try:
            response = requests.delete(base_url, headers=headers)
        except requests.HTTPError:
            self.logger.error('There was an issue with the delete user request double check the user name: %s'
                              % user_principal_name)
            raise
        if response.status_code == 204:
            success = True
            return {'success': success}
        else:
            self.logger.error('The response from Microsoft Office indicated something went wrong %s'
                              % response.status_code)
            self.logger.error(response.json())
            raise requests.HTTPError

    def test(self):
        if self.connection.access_token:
            return {'success': True}
        else:
            raise Exception('could not retrieve access token check your connection information')
