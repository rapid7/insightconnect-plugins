import insightconnect_plugin_runtime

# Custom imports below
from komand_active_directory_ldap.util.utils import UserAccountFlags
from .schema import UnlockUserInput, UnlockUserOutput, Input, Output, Component


class UnlockUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="unlock_user", description=Component.DESCRIPTION, input=UnlockUserInput(), output=UnlockUserOutput()
        )

    def run(self, params={}):
        return {
            Output.SUCCESS: self.connection.client.unblock_user(
                params.get(Input.DISTINGUISHED_NAME), UserAccountFlags.LOCKOUT
            )
        }
