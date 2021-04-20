import insightconnect_plugin_runtime
from .schema import ListIPAddressesRiskRulesInput, ListIPAddressesRiskRulesOutput, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_recorded_future.util.api import Endpoint


class ListIPAddressesRiskRules(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_IP_addresses_risk_rules",
            description=Component.DESCRIPTION,
            input=ListIPAddressesRiskRulesInput(),
            output=ListIPAddressesRiskRulesOutput(),
        )

    def run(self, params={}):
        try:
            return {
                Output.RISK_RULES: self.connection.client.make_request(Endpoint.list_ip_risk_rules())
                .get("data", {})
                .get("results")
            }
        except AttributeError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
