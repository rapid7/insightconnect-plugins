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
        result = get_user_info(self.connection, user_id, self.logger)

        headers = self.connection.get_headers(self.connection.get_auth_token())
        endpoint_for_account_enabled = f"https://graph.microsoft.com/v1.0/{self.connection.tenant}/users/{user_id}?$select=accountEnabled"

        result_enabled = None
        try:
            result_enabled = requests.get(endpoint_for_account_enabled, headers=headers)
        except Exception:
            for counter in range(1, 6):
                self.logger.info(f"Get user enabled failed, trying again, attempt {counter}.")
                self.logger.info(f"Sleeping for 5 seconds...")
                time.sleep(5)
                try:
                    self.logger.info(f"Attempting to get user info.")
                    result_enabled = requests.get(endpoint_for_account_enabled, headers=headers)
                    break  # We didn't get an exception, so break the loop
                except Exception:
                    self.logger.info(f"Get user info failed.")
                    pass  # we got an exception, force pass and try again

        if not result_enabled or not result_enabled.status_code == 200:
            raise PluginException(cause="Get User Info failed.",
                                  assistance="Unexpected response from server.",
                                  data=str(result))

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
