import komand
from .schema import UnsuspendUserInput, UnsuspendUserOutput
# Custom imports below
import requests
import urllib


class UnsuspendUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='unsuspend_user',
                description='Unsuspend a user',
                input=UnsuspendUserInput(),
                output=UnsuspendUserOutput())

    def run(self, params={}):
        """ Get the user by email """
        email = params.get("email")
        okta_url = self.connection.okta_url

        url = requests.compat.urljoin(okta_url, '/api/v1/users/' + urllib.quote(email))

        """ Search for the user by email to get the ID """
        response = self.connection.session.get(url)
        data = response.json()

        if response.status_code != 200:
            self.logger.error('Okta: Lookup User by Email failed: ' + data['errorSummary'])
            return {'success': False}

        userid = data['id']
        """ Deactivate the user by id """
        url = requests.compat.urljoin(okta_url, '/api/v1/users/' + userid + '/lifecycle/unsuspend')
        response = self.connection.session.post(url)
        if response.status_code == 404:
            raise Exception('Okta: Unsuspend User failed with status code 404: User not found by ID after retrieving ID via email')
        elif response.status_code == 400:
            raise Exception('Okta: Unsuspend User failed with status code 400: User was already unsuspended or in a state where they could not be unsuspended')
        elif response.status_code == 401:
            raise Exception('Okta: Invalid token or domain')
        return {'email': email, 'user_id': userid, 'success': True}
