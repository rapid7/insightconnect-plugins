import insightconnect_plugin_runtime
from .schema import ListAlertsForInvestigationInput, ListAlertsForInvestigationOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Investigations
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper

# Custom imports below
import json


class ListAlertsForInvestigation(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_alerts_for_investigation",
            description=Component.DESCRIPTION,
            input=ListAlertsForInvestigationInput(),
            output=ListAlertsForInvestigationOutput(),
        )

    def run(self, params={}):
        identifier = params.get(Input.ID)
        size = params.get(Input.SIZE)
        index = params.get(Input.INDEX)

        parameters = {"size": size, "index": index}

        request = ResourceHelper(self.connection.session, self.logger)

        endpoint = Investigations.list_alerts_for_investigation(self.connection.url, identifier)
        response = request.resource_request(endpoint, "get", params=parameters)

        try:
            result = json.loads(response.get("resource"))
        except json.decoder.JSONDecodeError:
            self.logger.error(f"InsightIDR response: {response}")
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )
        try:
            alerts = clean(result.get("data", {}))
            metadata = result.get("metadata", {})
            return {Output.ALERTS: alerts, Output.METADATA: metadata}
        except KeyError:
            self.logger.error(result)
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )
