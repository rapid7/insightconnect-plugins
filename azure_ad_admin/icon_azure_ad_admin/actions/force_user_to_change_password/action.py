import komand
from .schema import ForceUserToChangePasswordInput, ForceUserToChangePasswordOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
import requests


class ForceUserToChangePassword(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='force_user_to_change_password',
                description=Component.DESCRIPTION,
                input=ForceUserToChangePasswordInput(),
                output=ForceUserToChangePasswordOutput())

    def run(self, params={}):
        user_id = params.get(Input.USER_ID)
        endpoint = f"https://graph.microsoft.com/v1.0/{self.connection.tenant}/users/{user_id}"

        self.logger.info(f"Enabling user: {user_id}")

        headers = self.connection.get_headers(self.connection.get_auth_token())
        data = {
            "passwordProfile":
            {
                "forceChangePasswordNextSignIn": True
            }
        }
        result = requests.patch(endpoint, headers=headers, json=data)

        if not result.status_code == 204:
            raise PluginException(cause="Force User to Change Password failed.",
                                  assistance="Unexpected return code from server.",
                                  data=result.text)

        return {Output.SUCCESS: True}
