import insightconnect_plugin_runtime
from .schema import GetAlertEvidenceInput, GetAlertEvidenceOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Alerts
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper


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
        self.connection.session.headers["Accept-version"] = "strong-force-preview"
        request = ResourceHelper(self.connection.session, self.logger)
        params = {
            "size": params.get(Input.SIZE),
            "index": params.get(Input.INDEX)
        }
        self.logger.info(f"Getting the alert evidence for {alert_rrn}...")
        response = request.make_request(Alerts.get_alert_evidence(self.connection.url, alert_rrn), method="get", params=params)
        return {Output.EVIDENCES: response.get("evidences", []), Output.METADATA: response.get("metadata", {})}
