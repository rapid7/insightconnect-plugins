import insightconnect_plugin_runtime
from .schema import ReplaceIndicatorsInput, ReplaceIndicatorsOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Threats
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from komand_rapid7_insightidr.util.util import get_logging_context
import json


class ReplaceIndicators(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="replace_indicators",
            description=Component.DESCRIPTION,
            input=ReplaceIndicatorsInput(),
            output=ReplaceIndicatorsOutput(),
        )

    def run(self, params={}):
        request = ResourceHelper(self.connection.session, self.logger)
        endpoint = Threats.replace_indicators(self.connection.url, params.pop(Input.KEY))
        self.connection.session.headers["Accept-version"] = "investigations-preview"
        response = request.resource_request(endpoint, "post", params={"format": "json"}, payload=params)
        try:
            result = json.loads(response.get("resource"))
        except json.decoder.JSONDecodeError:
            self.logger.error(f"InsightIDR response: {response}", **get_logging_context())
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
                data=response,
            )
        return {
            Output.REJECTED_INDICATORS: result.get("rejected_indicators", []),
            Output.THREAT: result.get("threat", {}),
        }
