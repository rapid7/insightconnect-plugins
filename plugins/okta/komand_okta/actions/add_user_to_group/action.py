import insightconnect_plugin_runtime
from .schema import AddUserToGroupInput, AddUserToGroupOutput, Input, Output, Component

# Custom imports below


class AddUserToGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_user_to_group",
            description=Component.DESCRIPTION,
            input=AddUserToGroupInput(),
            output=AddUserToGroupOutput(),
        )

    def run(self, params={}):
        user_id = self.connection.api_client.get_user_id(params.get(Input.LOGIN))
        self.connection.api_client.add_user_to_group(user_id, params.get(Input.GROUPID))

        return {
            Output.USERID: user_id,
            Output.SUCCESS: True,
        }
