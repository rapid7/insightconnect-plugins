import insightconnect_plugin_runtime
from .schema import DisableAccountInput, DisableAccountOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1


class DisableAccount(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="disable_account",
            description=Component.DESCRIPTION,
            input=DisableAccountInput(),
            output=DisableAccountOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        account_identifiers = params.get(Input.ACCOUNT_IDENTIFIERS)
        # Make Action API Call
        self.logger.info("Making API Call...")
        multi_resp = {Output.MULTI_RESPONSE: []}
        for i in account_identifiers:
            response = client.disable_account(
                pytmv1.AccountTask(
                    accountName=i["account_name"], description=i.get("description", "")
                )
            )
            if "error" in response.result_code.lower():
                raise PluginException(
                    cause="An error occurred while disabling the account.",
                    assistance="Please check the account name and try again.",
                    data=response.errors,
                )
            else:
                multi_resp[Output.MULTI_RESPONSE].append(
                    response.response.dict().get("items")[0]
                )
        # Return results
        self.logger.info("Returning Results...")
        return multi_resp
