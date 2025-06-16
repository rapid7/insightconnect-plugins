import json
from typing import Dict, Any

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

from komand_rapid7_insightidr.util.endpoints import Investigations
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from komand_rapid7_insightidr.util.util import get_logging_context
from .schema import ListAlertsForInvestigationInput, ListAlertsForInvestigationOutput, Input, Output, Component


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
        self.connection.headers["Accept-version"] = "investigations-preview"
        request = ResourceHelper(self.connection.headers, self.logger)

        endpoint = Investigations.list_alerts_for_investigation(self.connection.url, identifier)
        response = request.resource_request(endpoint, "get", params=parameters)
        try:
            result = json.loads(response.get("resource"))
        except json.decoder.JSONDecodeError:
            self.logger.error(f"InsightIDR response: {response}", **self.connection.cloud_log_values)
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )
        self._get_rule_rrn(result)
        try:
            alerts = clean(result.get("data", {}))
            metadata = result.get("metadata", {})
            return {Output.ALERTS: alerts, Output.METADATA: metadata}
        except KeyError:
            self.logger.error(f"{result} {get_logging_context}")
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )

    @staticmethod
    def _get_rule_rrn(result: Dict[str, Any]) -> None:
        """
        Retrieve rule rrn from all records,
        due to inconsistent API from insightIDR
        """
        for data in result.get("data"):
            if isinstance(data.get("detection_rule_rrn"), dict):
                data["detection_rule_rrn"] = data.get("detection_rule_rrn", {}).get("rule_rrn", "")
