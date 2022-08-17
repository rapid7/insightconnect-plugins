import insightconnect_plugin_runtime
from .schema import AddUserInput, AddUserOutput, Input, Output, Component

# Custom imports below


class AddUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_user", description=Component.DESCRIPTION, input=AddUserInput(), output=AddUserOutput()
        )

    def run(self, params={}):
        return {Output.STATUS: self.connection.api.add_user(params).get("status")}
