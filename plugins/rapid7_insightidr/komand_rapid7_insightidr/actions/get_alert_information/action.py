import insightconnect_plugin_runtime
from .schema import GetAlertInformationInput, GetAlertInformationOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Alerts
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper


class GetAlertInformation(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_alert_information",
            description=Component.DESCRIPTION,
            input=GetAlertInformationInput(),
            output=GetAlertInformationOutput(),
        )

    def run(self, params={}):
        alert_rrn = params.get(Input.ALERT_RRN)
        self.connection.headers["Accept-version"] = "strong-force-preview"
        request = ResourceHelper(self.connection.headers, self.logger)
        self.logger.info(f"Getting the alert information for {alert_rrn}...", **request.logging_context)
        response = request.make_request(Alerts.get_alert_information(self.connection.url, alert_rrn), "get")
        return {Output.ALERT: response, Output.SUCCESS: True}
