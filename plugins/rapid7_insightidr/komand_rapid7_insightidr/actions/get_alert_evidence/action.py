import insightconnect_plugin_runtime
from .schema import GetAlertEvidenceInput, GetAlertEvidenceOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Alerts
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
import json


class GetAlertEvidence(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_alert_evidence",
            description=Component.DESCRIPTION,
            input=GetAlertEvidenceInput(),
            output=GetAlertEvidenceOutput(),
        )

    def run(self, params={}):
        alert_rrn = params.get(Input.ALERT_RRN)
        self.connection.headers["Accept-version"] = "strong-force-preview"
        request = ResourceHelper(self.connection.headers, self.logger)
        params = {"size": params.get(Input.SIZE), "index": params.get(Input.INDEX)}
        self.logger.info(f"Getting the alert evidence for {alert_rrn}...", **request.logging_context)
        response = request.make_request(
            Alerts.get_alert_evidence(self.connection.url, alert_rrn), method="get", params=params
        )

        evidences = response.get("evidences", [])

        for evidence in evidences:
            try:
                evidence["data"] = json.loads(evidence.get("data", ""))
            except Exception as error:
                self.logger.warning(f"data could not be convert to json - {error}")
                evidence["data"] = {}

        return {Output.EVIDENCES: response.get("evidences", []), Output.METADATA: response.get("metadata", {})}
