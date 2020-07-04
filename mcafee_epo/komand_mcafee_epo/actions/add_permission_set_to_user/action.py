import insightconnect_plugin_runtime
from .schema import AddPermissionSetToUserInput, AddPermissionSetToUserOutput, Output, Input
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class AddPermissionSetToUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_permission_set_to_user',
                description='Adds permission set(s) to specified user',
                input=AddPermissionSetToUserInput(),
                output=AddPermissionSetToUserOutput())

    def run(self, params={}):
        try:
            return {
                Output.MESSAGE: self.connection.client(
                    'core.addPermSetsForUser',
                    params.get(Input.USER),
                    params.get(Input.PERMISSION_SET)
                )
            }
        except Exception as e:
            raise PluginException(
                cause="Server Error",
                assistance=f"Could not add specified permission set to specified user. Error: {e}"
            )
