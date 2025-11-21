import insightconnect_plugin_runtime
from .schema import DeleteUserInput, DeleteUserOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class DeleteUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_user",
            description=Component.DESCRIPTION,
            input=DeleteUserInput(),
            output=DeleteUserOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        account_id = params.get(Input.ACCOUNT_ID, "")
        username = params.get(Input.USERNAME, "")
        # END INPUT BINDING - DO NOT REMOVE

        if self.connection.is_cloud and not account_id:
            raise PluginException(
                cause="Account ID not provided",
                assistance="Jira cloud server needs account ID to be set",
            )

        if not self.connection.is_cloud and not username:
            raise PluginException(
                cause="Username not provided",
                assistance="Jira server needs username to be set",
            )

        if not self.connection.is_cloud:
            success = self.connection.client.delete_user(username)
        else:
            success = self.connection.rest_client.delete_user(account_id)
        return {Output.SUCCESS: success}
