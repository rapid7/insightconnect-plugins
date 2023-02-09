import insightconnect_plugin_runtime
from .schema import GetUsersInput, GetUsersOutput, Input, Output, Component

# Custom imports below


class GetUsers(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_users", description=Component.DESCRIPTION, input=GetUsersInput(), output=GetUsersOutput()
        )

    def run(self, params={}):  # pylint: disable=unused-argument
        return {Output.USERS: self.connection.api.get_users().get("data", [])}
