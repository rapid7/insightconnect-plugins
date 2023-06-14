import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import convert_dict_to_camel_case
from .schema import GetUserByUsernameInput, GetUserByUsernameOutput, Input, Output, Component

# Custom imports below
from komand_duo_admin.util.helpers import clean
from komand_duo_admin.util.constants import Cause, Assistance


class GetUserByUsername(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user_by_username",
            description=Component.DESCRIPTION,
            input=GetUserByUsernameInput(),
            output=GetUserByUsernameOutput(),
        )

    def run(self, params={}):
        search_username = params.get(Input.USERNAME)
        self.logger.info(f"Searching for username or alias: {search_username}")
        result = self.connection.admin_api.get_user_by_username({"username": search_username}).get("response", {})
        if len(result) == 1:
            return {Output.USER: convert_dict_to_camel_case(clean(result[0]))}
        else:
            raise PluginException(cause=Cause.NOT_FOUND, assistance=Assistance.VERIFY_INPUT)
