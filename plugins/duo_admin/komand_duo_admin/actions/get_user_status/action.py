import insightconnect_plugin_runtime
from .schema import GetUserStatusInput, GetUserStatusOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_duo_admin.util.constants import Cause, Assistance


class GetUserStatus(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user_status",
            description=Component.DESCRIPTION,
            input=GetUserStatusInput(),
            output=GetUserStatusOutput(),
        )

    def run(self, params={}):
        users = self.connection.admin_api.get_user_by_username({"username": params.get(Input.USERNAME)}).get(
            "response", {}
        )
        if users and isinstance(users, list):
            user = users[0]
            return {Output.STATUS: user.get("status"), Output.USERID: user.get("user_id")}
        raise PluginException(cause=Cause.USER_NOT_FOUND, assistance=Assistance.USER_NOT_FOUND)
