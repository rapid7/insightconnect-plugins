import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import EnableUsersInput, EnableUsersOutput, Input, Output, Component
# Custom imports below


class EnableUsers(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='enable_users',
                description=Component.DESCRIPTION,
                input=EnableUsersInput(),
                output=EnableUsersOutput())

    def run(self, params={}):
        if len(params.get(Input.DISTINGUISHED_NAMES)) == 0:
            raise PluginException(
              cause="Distinguished Names must contain at least one entry",
              assistance="Please enter one or more Distinguished Names"
            )

        success = True
        enabled_users = self.connection.client.manage_users(params.get(Input.DISTINGUISHED_NAMES), True)
        if len(enabled_users.get("successes")) == 0:
            success = False

        return {
          Output.SUCCESS: success,
          Output.SUCCESSFUL_ENABLEMENTS: enabled_users.get("successes"),
          Output.UNSUCCESSFUL_ENABLEMENTS: enabled_users.get("failures")
        }
