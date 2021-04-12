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
        if self.connection.is_cloud and not params.get(Input.ACCOUNT_ID):
            raise PluginException(
                cause="Account ID not provided",
                assistance="Jira cloud server needs account ID to be set",
            )

        if not self.connection.is_cloud and not params.get(Input.USERNAME):
            raise PluginException(
                cause="Username not provided",
                assistance="Jira server needs username to be set",
            )

        if self.connection.is_cloud:
            success = self.connection.rest_client.delete_user(params.get(Input.ACCOUNT_ID))
        else:
            success = self.connection.client.delete_user(params.get(Input.USERNAME))
        return {Output.SUCCESS: success}
