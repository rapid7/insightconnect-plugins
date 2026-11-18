import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetAccountUsageInput, GetAccountUsageOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.util import constants, outputs


class GetAccountUsage(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_account_usage",
            description=Component.DESCRIPTION,
            input=GetAccountUsageInput(),
            output=GetAccountUsageOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        # END INPUT BINDING - DO NOT REMOVE

        result = self.connection.client.lookup("Get Account Usage", "GET", constants.PATH_ACCOUNT_USAGE)
        if not result.found:
            raise PluginException(
                cause=f"Get Account Usage: WhoisFreaks returned no usage record. WhoisFreaks said: {result.message}",
                assistance="Verify the API key in the plugin connection",
            )
        # WhoisFreaks echoes the API key in the usage record, it must never reach workflow output
        data = outputs.without_keys(result.data_dict, ("apiKey", "api_key", "apikey"))
        return outputs.compact(
            {
                Output.TOTAL_CREDITS: outputs.to_int(outputs.get_path(data, "apiCredits", "totalCredits")),
                Output.USED_CREDITS: outputs.to_int(outputs.get_path(data, "apiCredits", "servedRequest")),
                Output.SUBSCRIPTION_STATUS: outputs.to_str(
                    outputs.get_path(data, "apiSubscription", "subscriptionStatus")
                ),
                Output.SUBSCRIPTION_REQUEST_LIMIT: outputs.to_int(
                    outputs.get_path(data, "apiSubscription", "requestLimit")
                ),
                Output.SUBSCRIPTION_REQUESTS_USED: outputs.to_int(
                    outputs.get_path(data, "apiSubscription", "servedRequests")
                ),
                Output.RESPONSE: data,
            }
        )
