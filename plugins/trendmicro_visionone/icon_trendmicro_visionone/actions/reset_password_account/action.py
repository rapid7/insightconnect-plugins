import insightconnect_plugin_runtime
from .schema import (
    ResetPasswordAccountInput,
    ResetPasswordAccountOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1


class ResetPasswordAccount(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="reset_password_account",
            description=Component.DESCRIPTION,
            input=ResetPasswordAccountInput(),
            output=ResetPasswordAccountOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        account_identifiers = params.get(Input.ACCOUNT_IDENTIFIERS)
        # Build accounts list
        accounts = []
        for account_identifier in account_identifiers:
            accounts.append(
                pytmv1.AccountTask(
                    accountName=account_identifier["account_name"],
                    description=account_identifier.get(
                        "description", "Reset Account Password"
                    ),
                )
            )
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.reset_password_account(*accounts)
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while resetting the password for the account.",
                assistance="Please check the account name and try again.",
                data=response.errors,
            )
        # Return results
        self.logger.info("Returning Results...")
        return {Output.MULTI_RESPONSE: response.response.dict().get("items")}
