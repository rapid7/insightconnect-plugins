import insightconnect_plugin_runtime
from .schema import GetUserInfoInput, GetUserInfoOutput, Input, Output, Component

# Custom imports below
import requests
import time
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_azure_ad_admin.util.get_user_info import get_user_info


class GetUserInfo(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user_info",
            description=Component.DESCRIPTION,
            input=GetUserInfoInput(),
            output=GetUserInfoOutput(),
        )

    def run(self, params={}):
        user_id = params.get(Input.USER_ID)

        self.logger.info(f"Getting info for user: {user_id}")
        result = get_user_info(self.connection, user_id, self.logger)

        headers = self.connection.get_headers(self.connection.get_auth_token())
        endpoint_for_account_enabled = (
            f"https://graph.microsoft.com/v1.0/{self.connection.tenant}/users/{user_id}?$select=accountEnabled"
        )

        result_enabled = None
        try:
            result_enabled = requests.get(endpoint_for_account_enabled, headers=headers)
        except Exception:
            for counter in range(1, 6):
                self.logger.info(f"Get user enabled failed, trying again, attempt {counter}.")
                self.logger.info("Sleeping for 5 seconds...")
                time.sleep(5)
                try:
                    self.logger.info("Attempting to get user info.")
                    result_enabled = requests.get(endpoint_for_account_enabled, headers=headers)
                    break  # We didn't get an exception, so break the loop
                except Exception:
                    self.logger.info("Get user info failed.")

        if not result_enabled or not result_enabled.status_code == 200:
            raise PluginException(
                cause="Get User Info failed.",
                assistance="Unexpected response from server.",
                data=str(result),
            )

        try:
            account_enabled = result_enabled.json().get("accountEnabled")
        except Exception as e:
            raise PluginException(PluginException.Preset.INVALID_JSON) from e

        full_result = result.json()
        full_result["accountEnabled"] = account_enabled

        full_result = self._clean_empty_values(full_result)

        return {Output.USER_INFORMATION: full_result}

    def _clean_empty_values(self, input_dict):
        """return_non_empty. Cleans up recusively the dictionary

        :param input_dict:
        :type input_dict: Dict[str, Any]
        :rtype: Dict[Any, Any]
        """
        temp_dict = {}
        for key, value in input_dict.items():
            if value is not None and value != "":
                if isinstance(value, dict):
                    return_dict = self._clean_empty_values(value)
                    if return_dict:
                        temp_dict[key] = return_dict
                elif isinstance(value, list):
                    if len(value) > 0:
                        temp_dict[key] = value
                else:
                    temp_dict[key] = value
        return temp_dict
