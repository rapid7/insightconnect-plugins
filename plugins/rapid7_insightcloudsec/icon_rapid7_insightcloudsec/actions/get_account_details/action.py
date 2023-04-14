import insightconnect_plugin_runtime
from .schema import GetAccountDetailsInput, GetAccountDetailsOutput, Input, Output, Component

# Custom imports below


class GetAccountDetails(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_account_details",
            description=Component.DESCRIPTION,
            input=GetAccountDetailsInput(),
            output=GetAccountDetailsOutput(),
        )

    def run(self, params={}):
        return {Output.ACCOUNTDETAILS: self.connection.api.get_account_details(params.get(Input.ACCOUNTID))}
