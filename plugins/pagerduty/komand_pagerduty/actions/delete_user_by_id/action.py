import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import DeleteUserByIdInput, DeleteUserByIdOutput, Input, Output, Component

# Custom imports below
from komand_pagerduty.util.util import normalize_user


class DeleteUserById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_user_by_id",
            description="Delete a User By ID",
            input=DeleteUserByIdInput(),
            output=DeleteUserByIdOutput(),
        )

    def run(self, params={}):
        email = params.get(Input.EMAIL)
        user_id = params.get(Input.ID)

        self.connection.api.delete_user_by_id(email=email, user_id=user_id)

        return {Output.SUCCESS: f"The user {user_id} has been deleted"}
