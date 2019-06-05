import komand
from .schema import AssignUserToAppSsoInput, AssignUserToAppSsoOutput
# Custom imports below
import requests


class AssignUserToAppSso(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='assign_user_to_app_sso',
                description='Assign user to application for SSO and provisioning',
                input=AssignUserToAppSsoInput(),
                output=AssignUserToAppSsoOutput())

    def run(self, params={}):
        appid = params.get("applicationId")
        appuser = params.get("appuser")

        okta_url = self.connection.okta_url

        url = requests.compat.urljoin(okta_url, '/api/v1/apps/' + appid + '/users')

        response = self.connection.session.post(url, data=appuser)

        try:
            data = response.json()
        except ValueError:
            self.logger.error('An error has occurred: ' + response.content)
            raise Exception('An unexpected error has occurred')

        if 'errorSummary' in data:
            self.logger.error(data)
            raise Exception(data['errorSummary'])
