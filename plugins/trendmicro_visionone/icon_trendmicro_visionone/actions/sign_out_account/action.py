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
        # Make Action API Call
        self.logger.info("Making API Call...")
        multi_resp = []
        for account_identifier in account_identifiers:
            response = client.sign_out_account(
                pytmv1.AccountTask(
                    accountName=account_identifier["account_name"],
                    description=account_identifier.get("description", ""),
                )
            )
            if "error" in response.result_code.lower():
                raise PluginException(
                    cause="An error occurred while signing out the account.",
                    assistance="Please check the Account Identifier and try again.",
                    data=response.errors,
                )
            multi_resp.append(response.response.dict().get("items")[0])
        # Return results
        self.logger.info("Returning Results...")
        return {Output.MULTI_RESPONSE: multi_resp}
