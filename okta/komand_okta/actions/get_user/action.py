import komand
from .schema import GetUserInput, GetUserOutput, Input, Output, Component
# Custom imports below
import requests
import urllib.parse
from komand.exceptions import PluginException


class GetUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_user',
            description=Component.DESCRIPTION,
            input=GetUserInput(),
            output=GetUserOutput())

    def run(self, params={}):
        """ Get the user by email """
        url = requests.compat.urljoin(
            self.connection.okta_url,
            f'/api/v1/users/{urllib.parse.quote(params.get(Input.EMAIL))}'
        )

        """ Search for the user by email to get the ID """
        response = self.connection.session.get(url)
        data = response.json()
        data[Output.FOUND] = True

        if response.status_code == 200:
            return komand.helper.clean(data)

        if 'errorSummary' in data:
            if response.status_code == 404:
                summary = data['errorSummary']
                self.logger.error(f'Okta: Lookup User by Email failed: {summary}')
                return {Output.FOUND: False}

        if response.status_code == 401:
            self.logger.error('Okta: Invalid token or domain')

        raise PluginException(cause='Okta: An error occurred')
