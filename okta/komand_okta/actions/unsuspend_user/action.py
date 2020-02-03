import komand
from .schema import UnsuspendUserInput, UnsuspendUserOutput, Input, Output, Component
# Custom imports below
import requests
import urllib.parse
from komand.exceptions import PluginException


class UnsuspendUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='unsuspend_user',
            description=Component.DESCRIPTION,
            input=UnsuspendUserInput(),
            output=UnsuspendUserOutput())

    def run(self, params={}):
        """ Get the user by email """
        email = params.get(Input.EMAIL)
        url = requests.compat.urljoin(
            self.connection.okta_url,
            f'/api/v1/users/{urllib.parse.quote(email)}'
        )

        """ Search for the user by email to get the ID """
        response = self.connection.session.get(url)
        data = response.json()

        if response.status_code != 200:
            summary = data['errorSummary']
            self.logger.error(f'Okta: Lookup User by Email failed: {summary}')
            return {Output.SUCCESS: False}

        user_id = data['id']
        """ Deactivate the user by id """
        url = requests.compat.urljoin(self.connection.okta_url, f'/api/v1/users/{user_id}/lifecycle/unsuspend')
        response = self.connection.session.post(url)
        if response.status_code == 404:
            raise PluginException(
                cause='Unsuspend User failed',
                assistance='Okta: Unsuspend User failed with status code 404: User not found by ID after retrieving ID via email'
            )
        elif response.status_code == 400:
            raise PluginException(
                cause='Unsuspend User failed',
                assistance='Okta: Unsuspend User failed with status code 400: User was already unsuspended or in a state where they could not be unsuspended'
            )
        elif response.status_code == 401:
            raise PluginException(PluginException.Preset.API_KEY)
        return {Output.EMAIL: email, Output.USER_ID: user_id, Output.SUCCESS: True}
