import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import EnableUsersInput, EnableUsersOutput, Input, Output, Component

# Custom imports below


class EnableUsers(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="enable_users",
            description=Component.DESCRIPTION,
            input=EnableUsersInput(),
            output=EnableUsersOutput(),
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

        enabled_users = self.connection.client.manage_users(distinguished_names, True)
        return {
            Output.COMPLETED: enabled_users.get("successes"),
            Output.FAILED: enabled_users.get("failures"),
        }
