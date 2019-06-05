import komand
from .schema import SuspendUserInput, SuspendUserOutput
# Custom imports below
import requests
import urllib


class SuspendUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='suspend_user',
                description='Suspend a user',
                input=SuspendUserInput(),
                output=SuspendUserOutput())

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
        url = requests.compat.urljoin(okta_url, '/api/v1/users/' + userid + '/lifecycle/suspend')
        response = self.connection.session.post(url)
        if response.status_code == 404:
            raise Exception('Okta: Suspend User failed with status code 404: User not found by ID after retrieving ID via email')
        elif response.status_code == 400:
            raise Exception('Okta: Suspend User failed with status code 400: User was already suspended or in a state where they could not be suspended')
        elif response.status_code == 401:
            raise Exception('Okta: Invalid token or domain')

        return {'email': email, 'user_id': userid, 'success': True}
