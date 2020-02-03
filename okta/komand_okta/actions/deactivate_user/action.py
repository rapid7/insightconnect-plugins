import komand
from .schema import DeactivateUserInput, DeactivateUserOutput, Input, Output, Component
# Custom imports below
import requests
from komand_okta.util import helpers
from komand.exceptions import PluginException


class DeactivateUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='deactivate_user',
            description=Component.DESCRIPTION,
            input=DeactivateUserInput(),
            output=DeactivateUserOutput())

    def run(self, params={}):
        """ Get the user by email """
        email = params.get(Input.EMAIL)
        user_id = helpers.get_user_id(email, self.connection, self.logger)

        if user_id is None:
            return {Output.SUCCESS: False}

        """ Deactivate the user by id """
        url = requests.compat.urljoin(self.connection.okta_url, f'/api/v1/users/{user_id}/lifecycle/deactivate')
        response = self.connection.session.post(url)

        if response.status_code == 401:
            raise PluginException(
                PluginException.Preset.API_KEY
            )

        if response.status_code != 200:
            raise PluginException(cause='Okta Deactivate User failed',
                                  assistance=f'Okta Deactivate User failed with status code: {response.status_code}')

        return {Output.EMAIL: email, Output.USER_ID: user_id, Output.SUCCESS: True}
