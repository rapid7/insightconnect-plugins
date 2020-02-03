import komand
from .schema import AssignUserToAppSsoInput, AssignUserToAppSsoOutput, Input, Component
# Custom imports below
import requests
from komand.exceptions import PluginException


class AssignUserToAppSso(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='assign_user_to_app_sso',
            description=Component.DESCRIPTION,
            input=AssignUserToAppSsoInput(),
            output=AssignUserToAppSsoOutput())

    def run(self, params={}):
        app_id = params.get(Input.APPLICATIONID)
        app_user = params.get(Input.APPUSER)
        okta_url = self.connection.okta_url

        url = requests.compat.urljoin(okta_url, '/api/v1/apps/' + app_id + '/users')
        response = self.connection.session.post(url, data=app_user)

        try:
            data = response.json()
        except ValueError:
            self.logger.error('An error has occurred: ' + response.content)
            raise PluginException(cause='An unexpected error has occurred', assistance=response.content)

        if 'errorSummary' in data:
            self.logger.error(data)
            raise PluginException(cause='An unexpected error has occurred', assistance=data['errorSummary'])
