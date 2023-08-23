import insightconnect_plugin_runtime
from .schema import SignOutAccountInput, SignOutAccountOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1


class SignOutAccount(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="sign_out_account",
            description=Component.DESCRIPTION,
            input=SignOutAccountInput(),
            output=SignOutAccountOutput(),
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
                    description=account_identifier.get("description", ""),
                )
            )
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.sign_out_account(*accounts)
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while signing out the account.",
                assistance="Please check the Account Identifier and try again.",
                data=response.errors,
            )
        # Return results
        self.logger.info("Returning Results...")
        return {Output.MULTI_RESPONSE: response.response.dict().get("items")}
