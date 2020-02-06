import komand
from .schema import DeleteUserInput, DeleteUserOutput, Input, Output, Component
# Custom imports below
import requests
import urllib.parse
from komand.exceptions import PluginException


class DeleteUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='delete_user',
            description=Component.DESCRIPTION,
            input=DeleteUserInput(),
            output=DeleteUserOutput())

    def run(self, params={}):
        # Get the user by email
        email = params.get(Input.USER_EMAIL)
        okta_url = self.connection.okta_url

        url = requests.compat.urljoin(okta_url, f"/api/v1/users/{urllib.parse.quote(email)}")

        # Search for the user by email to get the id
        response = self.connection.session.get(url)

        if response.status_code != 200:
            self.logger.error(f"Okta: Lookup User by Email failed: {response.text}")
            return {Output.SUCCESS: False}

        data = response.json()

        user_id = data['id']
        send_email_param = {
            "sendEmail": params.get(Input.SEND_ADMIN_EMAIL)
        }

        # Deactivate the user by id
        self.logger.info(f"Deactivating user ID: {user_id}")
        url = requests.compat.urljoin(okta_url, f"/api/v1/users/{user_id}")
        response = self.connection.session.delete(url, params=send_email_param)

        if response.status_code == 401:
            self.logger.error("Okta: Invalid token or domain")

        if response.status_code >= 400:
            raise PluginException(cause="Delete User failed.",
                                  assistance=f"Okta Deactivate User failed. Response was: {response.text}")

        return {Output.SUCCESS: True}
