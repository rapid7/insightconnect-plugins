import insightconnect_plugin_runtime
from .schema import ListUrlRiskRulesInput, ListUrlRiskRulesOutput, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_recorded_future.util.api import Endpoint


class ListUrlRiskRules(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_url_risk_rules",
            description=Component.DESCRIPTION,
            input=ListUrlRiskRulesInput(),
            output=ListUrlRiskRulesOutput(),
        )

    def run(self, params={}):
        try:
            return {
                Output.RISK_RULES: self.connection.client.make_request(Endpoint.list_url_risk_rules())
                .get("data", {})
                .get("results")
            }
        except AttributeError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
