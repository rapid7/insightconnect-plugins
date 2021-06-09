import komand

# Custom imports below
from komand_active_directory_ldap.util.utils import ADUtils
from .schema import DisableUserInput, DisableUserOutput, Input, Output


class DisableUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="disable_user",
            description="Disable a account",
            input=DisableUserInput(),
            output=DisableUserOutput(),
        )

    def run(self, params={}):
        return {
            Output.SUCCESS: ADUtils.change_account_status(
                self.connection.conn, params.get(Input.DISTINGUISHED_NAME), False, self.logger
            )
        }
