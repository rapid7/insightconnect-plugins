import komand

# Custom imports below
from komand_active_directory_ldap.util.utils import ADUtils
from .schema import EnableUserInput, EnableUserOutput, Input, Output


class EnableUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="enable_user",
            description="Enable a account",
            input=EnableUserInput(),
            output=EnableUserOutput(),
        )

    def run(self, params={}):
        return {
            Output.SUCCESS: ADUtils.change_account_status(
                self.connection.conn,
                params.get(Input.DISTINGUISHED_NAME),
                True,
                self.logger
            )
        }
