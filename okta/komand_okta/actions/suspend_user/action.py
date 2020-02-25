import komand
from .schema import SuspendUserInput, SuspendUserOutput, Input, Output, Component
# Custom imports below
import requests
from komand_okta.util import helpers
from komand.exceptions import PluginException


class SuspendUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='suspend_user',
            description=Component.DESCRIPTION,
            input=SuspendUserInput(),
            output=SuspendUserOutput())

    def run(self, params={}):
        """ Get the user by email """
        email = params.get(Input.EMAIL)
        user_id = helpers.get_user_id(email, self.connection, self.logger)

        if user_id is None:
            return {Output.SUCCESS: False}

        """ Deactivate the user by id """
        url = requests.compat.urljoin(self.connection.okta_url, f'/api/v1/users/{user_id}/lifecycle/suspend')
        response = self.connection.session.post(url)

        if response.status_code == 404:
            raise PluginException(
                cause='Suspend User failed',
                assistance='Okta: Suspend User failed with status code 404: User not found by ID after retrieving ID via email'
            )
        elif response.status_code == 400:
            raise PluginException(
                cause='Suspend User failed',
                assistance='Okta: Suspend User failed with status code 400: User was already suspended or in a state where they could not be suspended'
            )
        elif response.status_code == 401:
            raise PluginException(
                PluginException.Preset.API_KEY
            )

        return {Output.EMAIL: email, Output.USER_ID: user_id, Output.SUCCESS: True}
