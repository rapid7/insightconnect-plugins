import insightconnect_plugin_runtime
from .schema import GetAccountInformationInput, GetAccountInformationOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from komand_rapid7_insightidr.util.endpoints import Accounts
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
import json


class GetAccountInformation(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_account_information",
            description=Component.DESCRIPTION,
            input=GetAccountInformationInput(),
            output=GetAccountInformationOutput(),
        )

    def run(self, params={}):
        account_rrn = params.get(Input.ACCOUNT_RRN)
        self.connection.headers["Accept-version"] = "strong-force-preview"
        endpoint = Accounts.get_account(self.connection.url, account_rrn)
        request = ResourceHelper(self.connection.headers, self.logger)
        self.logger.info(f"Getting the account information for {account_rrn}...", **self.connection.cloud_log_values)
        response = request.make_request(endpoint, "get")
        return {Output.ACCOUNT: response}
