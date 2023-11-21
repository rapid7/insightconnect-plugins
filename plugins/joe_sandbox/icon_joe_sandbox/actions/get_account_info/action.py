import insightconnect_plugin_runtime
from .schema import GetAccountInfoInput, GetAccountInfoOutput, Input, Output, Component
# Custom imports below


class GetAccountInfo(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="get_account_info",
                description=Component.DESCRIPTION,
                input=GetAccountInfoInput(),
                output=GetAccountInfoOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        # END INPUT BINDING - DO NOT REMOVE
        # TODO - If input bindings for connection can be done check to same if it you can do the same here
        self.logger.info('Running account_info')
        account_info = self.connection.api.account_info()
        
        self.logger.info(account_info)

        return account_info
