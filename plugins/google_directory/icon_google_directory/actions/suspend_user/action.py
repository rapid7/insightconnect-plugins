import insightconnect_plugin_runtime
from .schema import SuspendUserInput, SuspendUserOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class SuspendUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="suspend_user",
            description=Component.DESCRIPTION,
            input=SuspendUserInput(),
            output=SuspendUserOutput(),
        )

    def run(self, params={}):
        user = (
            self.connection.service.users().update(userKey=params.get(Input.EMAIL), body={"suspended": True}).execute()
        )
        if "suspended" in user:
            return {Output.SUCCESS: user.get("suspended")}
        else:
            raise PluginException(
                cause="Suspend status was not found in the server response.",
                assistance="Please check and verify the status of the user.",
            )
