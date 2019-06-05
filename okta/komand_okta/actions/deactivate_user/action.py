import komand
from .schema import DeactivateUserInput, DeactivateUserOutput
# Custom imports below
import requests
import urllib


class DeactivateUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='deactivate_user',
                description='Deactivate a user',
                input=DeactivateUserInput(),
                output=DeactivateUserOutput())

    def run(self, params={}):
        """ Get the user by email """
        email = params.get("email")
        okta_url = self.connection.okta_url

        url = requests.compat.urljoin(okta_url, '/api/v1/users/' + urllib.quote(email))

        """ Search for the user by email to get the id """
        response = self.connection.session.get(url)
        data = response.json()

        if response.status_code != 200:
            self.logger.error('Okta: Lookup User by Email failed: ' + data['errorSummary'])
            return {'success': False}

        userid = data['id']
        """ Deactivate the user by id """
        url = requests.compat.urljoin(okta_url, '/api/v1/users/' + userid + '/lifecycle/deactivate')
        response = self.connection.session.post(url)

        if response.status_code == 401:
            self.logger.error('Okta: Invalid token or domain')

        if response.status_code != 200:
            raise Exception('Okta Deactivate User failed with status code: ' + str(response.status_code))
        return {'email': email, 'user_id': userid, 'success': True}

    def test(self):
        return {'success': True}
