import insightconnect_plugin_runtime
from .schema import SuspendUserInput, SuspendUserOutput

# Custom imports below


class SuspendUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="suspend_user",
            description="Suspend a User",
            input=SuspendUserInput(),
            output=SuspendUserOutput(),
        )

    def run(self, params={}):
        body = {"suspended": True}
        user = self.connection.service.users().update(userKey=params["user"], body=body).execute()
        return {"user": user}
