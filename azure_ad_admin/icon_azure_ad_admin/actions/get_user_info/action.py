import komand
from .schema import GetUserInfoInput, GetUserInfoOutput, Input, Output, Component
# Custom imports below
import requests
import time
from komand.exceptions import PluginException
from icon_azure_ad_admin.util.get_user_info import get_user_info



class GetUserInfo(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_user_info',
            description=Component.DESCRIPTION,
            input=GetUserInfoInput(),
            output=GetUserInfoOutput())

    def run(self, params={}):
        user_id = params.get(Input.USER_ID)

        self.logger.info(f"Getting info for user: {user_id}")
        result = get_user_info(self.connection, user_id)

        headers = self.connection.get_headers(self.connection.get_auth_token())
        endpoint_for_account_enabled = f"https://graph.microsoft.com/v1.0/{self.connection.tenant}/users/{user_id}?$select=accountEnabled"
        result_enabled = requests.get(endpoint_for_account_enabled, headers=headers)

        if not result_enabled.status_code == 200:
            self.logger.info("Get account enabled failed, retrying...")
            time.sleep(5)  # adding retry
            result_enabled = requests.get(endpoint_for_account_enabled, headers=headers)
            if not result_enabled.status_code == 200:
                raise PluginException(cause="Get User Info failed.",
                                      assistance="Unexpected return code from server.",
                                      data=result.text)

        try:
            account_enabled = result_enabled.json().get("accountEnabled")
        except Exception as e:
            raise PluginException(PluginException.Preset.INVALID_JSON) from e

        full_result = result.json()
        full_result["accountEnabled"] = account_enabled

        # I didn't want to use clean in case a user is looking for a key that came back as null
        # businessPhones is a list, thus the special check for that key
        for key in full_result.keys():
            if not full_result.get(key):
                if not key == "businessPhones":
                    full_result[key] = ""
                else:
                    full_result[key] = []

        return {Output.USER_INFORMATION: full_result}
