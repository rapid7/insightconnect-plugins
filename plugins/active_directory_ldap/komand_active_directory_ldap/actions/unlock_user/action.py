import komand
from .schema import UnlockUserInput, UnlockUserOutput, Input, Output, Component
from komand_active_directory_ldap.util.utils import ADUtils, UserAccountFlags

# Custom imports below


class UnlockUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="unlock_user", description=Component.DESCRIPTION, input=UnlockUserInput(), output=UnlockUserOutput()
        )

    def run(self, params={}):
        user_flag = UserAccountFlags.LOCKOUT
        unlock_user = True
        return {
            Output.SUCCESS: ADUtils.change_useraccountcontrol_property(
                self.connection.conn, params.get(Input.DISTINGUISHED_NAME), unlock_user, user_flag, self.logger
            )
        }
