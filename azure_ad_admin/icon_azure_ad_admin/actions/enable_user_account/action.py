import komand
import requests
# Custom imports below
from komand.exceptions import PluginException

from .schema import EnableUserAccountInput, EnableUserAccountOutput, Input, Output, Component


class EnableUserAccount(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='enable_user_account',
            description=Component.DESCRIPTION,
            input=EnableUserAccountInput(),
            output=EnableUserAccountOutput())

    def run(self, params={}):
        user_id = params.get(Input.USER_ID)
        endpoint = f"https://graph.microsoft.com/v1.0/{self.connection.tenant}/users/{user_id}"

        self.logger.info(f"Enabling user: {user_id}")

        headers = self.connection.get_headers(self.connection.get_auth_token())
        data = {
            "accountEnabled": True
        }
        result = requests.patch(endpoint, headers=headers, json=data)

        if not result.status_code == 204:
            raise PluginException(cause="Enable user failed.",
                                  assistance="Unexpected return code from server.",
                                  data=result.text)

        return {Output.SUCCESS: True}
