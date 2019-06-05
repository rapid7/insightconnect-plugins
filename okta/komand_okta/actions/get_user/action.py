import komand
from .schema import GetUserInput, GetUserOutput
# Custom imports below
import requests
import urllib


class GetUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_user',
                description='Obtain information about a user',
                input=GetUserInput(),
                output=GetUserOutput())

    def run(self, params={}):
        email = params.get("email")
        okta_url = self.connection.okta_url

        url = requests.compat.urljoin(okta_url, '/api/v1/users/' + urllib.quote(email))

        """ Search for the user by email to get the ID """
        response = self.connection.session.get(url)
        data = response.json()
        data['found'] = True

        if response.status_code == 200:
            return komand.helper.clean(data)

        if 'errorSummary' in data:

            if response.status_code == 404:
                self.logger.error('Okta: Lookup User by Email failed: ' + data['errorSummary'])
                return {'found': False}

        if response.status_code == 401:
            self.logger.error('Okta: Invalid token or domain')

        raise Exception('Okta: An error occurred')

    def test(self):
        return {'found': False}
