import insightconnect_plugin_runtime
from .schema import GetAccountInfoInput, GetAccountInfoOutput, Output, Component

# Custom imports below


class GetAccountInfo(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_account_info",
            description=Component.DESCRIPTION,
            input=GetAccountInfoInput(),
            output=GetAccountInfoOutput(),
        )

    def run(self):
        account_info = self.connection.api.account_info()
        return {Output.TYPE: account_info.get("type"), Output.QUOTA: account_info.get("quota")}
