import komand
from .schema import ResetFactorsInput, ResetFactorsOutput
# Custom imports below
import requests
import urllib


class ResetFactors(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='reset_factors',
                description='Reset all multifactor authentications for user by email',
                input=ResetFactorsInput(),
                output=ResetFactorsOutput())

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

        """ Get enrolled factors by user id """
        url = requests.compat.urljoin(okta_url, '/api/v1/users/' + userid + '/factors')
        response = self.connection.session.get(url)
        data = response.json()

        """ Reset all factors """
        for factor in data:
            url = requests.compat.urljoin(okta_url, '/api/v1/users/' + userid + '/factors/' + factor['id'])
            response = self.connection.session.delete(url)

            if response.status_code != 204:
                data = response.json()
                self.logger.error('Okta: {} error. Error code: {}. {}'.format(response.status_code,
                                  data['errorCode'], data['errorSummary']))
                raise Exception(data['errorSummary'])

        return {'email': email, 'user_id': userid, 'success': True}
