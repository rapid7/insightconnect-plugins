import insightconnect_plugin_runtime
from .schema import SearchHashesInput, SearchHashesOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_recorded_future.util.util import AvailableInputs
from komand_recorded_future.util.api import Endpoint


class SearchHashes(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_hashes",
            description=Component.DESCRIPTION,
            input=SearchHashesInput(),
            output=SearchHashesOutput(),
        )

    def run(self, params={}):
        params["fields"] = AvailableInputs.HashFields
        risk_rule = AvailableInputs.HashRiskRuleMap.get(params.get(Input.RISKRULE))
        if risk_rule:
            params[Input.RISKRULE] = risk_rule
        else:
            params[Input.RISKRULE] = None
        try:
            return {
                Output.DATA: insightconnect_plugin_runtime.helper.clean(
                    self.connection.client.make_request(Endpoint.search_hashes(), params).get("data", {}).get("results")
                )
            }
        except AttributeError as e:
            raise PluginException(
                cause="Recorded Future returned unexpected response.",
                assistance="Please check that the provided inputs are correct and try again.",
                data=e,
            )
