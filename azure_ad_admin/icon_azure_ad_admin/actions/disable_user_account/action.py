import komand
import requests
# Custom imports below
from komand.exceptions import PluginException

from .schema import DisableUserAccountInput, DisableUserAccountOutput, Input, Output, Component


# NOTE: You need to add your app to the Global Admin role
# https://social.msdn.microsoft.com/Forums/azure/en-US/c7e2507c-35c4-43c0-a5db-41973611e356/authorizationrequestdeniedquot-quotinsufficient-privileges-to-complete-the-operationquot?forum=WindowsAzureAD
class DisableUserAccount(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='disable_user_account',
            description=Component.DESCRIPTION,
            input=DisableUserAccountInput(),
            output=DisableUserAccountOutput())

    def run(self, params={}):
        user_id = params.get(Input.USER_ID)
        endpoint = f"https://graph.microsoft.com/v1.0/{self.connection.tenant}/users/{user_id}"

        self.logger.info(f"Disabling user: {user_id}")

        headers = self.connection.get_headers(self.connection.get_auth_token())
        data = {
            "accountEnabled": False
        }
        result = requests.patch(endpoint, headers=headers, json=data)

        if not result.status_code == 204:
            raise PluginException(cause="Disable user failed.",
                                  assistance="Unexpected return code from server.",
                                  data=result.text)

        return {Output.SUCCESS: True}
