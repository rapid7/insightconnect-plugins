import komand
from .schema import (
    AddIndicatorsToAThreatInput,
    AddIndicatorsToAThreatOutput,
    Input,
    Output,
    Component,
)
from komand.exceptions import PluginException

# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Threats
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
import json


class AddIndicatorsToAThreat(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_indicators_to_a_threat",
            description=Component.DESCRIPTION,
            input=AddIndicatorsToAThreatInput(),
            output=AddIndicatorsToAThreatOutput(),
        )

    def run(self, params={}):
        request = ResourceHelper(self.connection.session, self.logger)
        endpoint = Threats.add_indicators_to_a_threat(self.connection.url, params.pop(Input.KEY))

        response = request.resource_request(
            endpoint, "post", params={"format": "json"}, payload=params
        )
        try:
            result = json.loads(response["resource"])
        except json.decoder.JSONDecodeError:
            self.logger.error(f"InsightIDR response: {response}")
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
                data=response,
            )
        return {
            Output.REJECTED_INDICATORS: result["rejected_indicators"],
            Output.THREAT: result["threat"],
        }
