import insightconnect_plugin_runtime
from .schema import GetAccountsInput, GetAccountsOutput, Input, Output, Component

# Custom imports below
from icon_cloudflare.util.helpers import clean, convert_dict_keys_to_camel_case


class GetAccounts(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="getAccounts", description=Component.DESCRIPTION, input=GetAccountsInput(), output=GetAccountsOutput()
        )

    def run(self, params={}):
        parameters = {
            "name": params.get(Input.NAME),
            "page": params.get(Input.PAGE),
            "per_page": params.get(Input.PERPAGE),
            "direction": params.get(Input.DIRECTION),
        }
        return {
            Output.ACCOUNTS: convert_dict_keys_to_camel_case(
                self.connection.api_client.get_accounts(clean(parameters)).get("result", [])
            )
        }
