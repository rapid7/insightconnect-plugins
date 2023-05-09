import insightconnect_plugin_runtime
from .schema import RemoveUserFromGroupInput, RemoveUserFromGroupOutput, Input, Output, Component

# Custom imports below


class RemoveUserFromGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove_user_from_group",
            description=Component.DESCRIPTION,
            input=RemoveUserFromGroupInput(),
            output=RemoveUserFromGroupOutput(),
        )

    def run(self, params={}):
        user_id = self.connection.api_client.get_user_id(params.get(Input.LOGIN))
        return {
            Output.SUCCESS: self.connection.api_client.remove_user_from_group(user_id, params.get(Input.GROUPID)),
            Output.USERID: user_id,
        }
