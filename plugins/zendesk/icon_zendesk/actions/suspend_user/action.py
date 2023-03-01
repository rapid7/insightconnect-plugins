import insightconnect_plugin_runtime
from .schema import SuspendUserInput, SuspendUserOutput, Input, Output

# Custom imports below


class SuspendUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="suspend_user",
            description="Suspend user",
            input=SuspendUserInput(),
            output=SuspendUserOutput(),
        )

    def run(self, params={}):
        user_id = params.get(Input.USER_ID)

        status = False
        try:
            user = self.connection.client.users(id=user_id)
            user.suspended = "true"
            suspend = self.connection.client.users.update(user)
            status = True if suspend.suspended else False
            self.logger.debug(suspend.suspended)
        except Exception as error:
            self.logger.debug(error)
        return {Output.STATUS: status}
