import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import DisableUsersInput, DisableUsersOutput, Input, Output, Component

# Custom imports below
from komand_active_directory_ldap.util.utils import ADUtils


class DisableUsers(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="disable_users",
            description=Component.DESCRIPTION,
            input=DisableUsersInput(),
            output=DisableUsersOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        distinguished_names = params.get(Input.DISTINGUISHED_NAMES)
        # END INPUT BINDING - DO NOT REMOVE

        if not distinguished_names:
            raise PluginException(
                cause="Distinguished Names must contain at least one entry",
                assistance="Please enter one or more Distinguished Names",
            )

        disabled_users = self.connection.client.manage_users(distinguished_names, False)
        return {
            Output.COMPLETED: disabled_users.get("successes"),
            Output.FAILED: disabled_users.get("failures"),
        }
