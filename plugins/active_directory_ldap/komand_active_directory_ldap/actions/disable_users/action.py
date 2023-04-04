import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import DisableUsersInput, DisableUsersOutput, Input, Output, Component
# Custom imports below


class DisableUsers(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='disable_users',
                description=Component.DESCRIPTION,
                input=DisableUsersInput(),
                output=DisableUsersOutput())

    def run(self, params={}):
        if len(params.get(Input.DISTINGUISHED_NAMES)) == 0:
            raise PluginException(
              cause="Distinguished Names must contain at least one entry",
              assistance="Please enter one or more Distinguished Names"
            )

        success = True
        disabled_users = self.connection.client.manage_users(params.get(Input.DISTINGUISHED_NAMES), False)
        if len(disabled_users.get("successes")) == 0:
            success = False

        return {
          Output.SUCCESS: success,
          Output.SUCCESSFUL_DISABLEMENTS: disabled_users.get("successes"),
          Output.UNSUCCESSFUL_DISABLEMENTS: disabled_users.get("failures")
        }

