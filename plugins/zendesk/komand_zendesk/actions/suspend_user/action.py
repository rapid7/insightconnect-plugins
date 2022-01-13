import insightconnect_plugin_runtime
from .schema import SuspendUserInput, SuspendUserOutput, Input, Output

# Custom imports below
import zenpy


class SuspendUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="suspend_user",
            description="Suspend user",
            input=SuspendUserInput(),
            output=SuspendUserOutput(),
        )

    def run(self, params={}):
        client = self.connection.client
        try:
            user = client.users(id=params.get(Input.USER_ID))
            user.suspended = "true"
            suspend = client.users.update(user)
            self.logger.debug(suspend.suspended)
            if suspend.suspended:
                return {Output.STATUS: True}
            else:
                return {Output.STATUS: False}
        except zenpy.lib.exception.APIException as e:
            self.logger.debug(e)
            return {Output.STATUS: False}

    def test(self):
        try:
            test = self.connection.client.users.me().email
            return {"success": test}
        except:
            raise
