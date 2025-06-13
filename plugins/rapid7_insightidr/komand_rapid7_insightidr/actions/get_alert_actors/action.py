import insightconnect_plugin_runtime
from .schema import GetAlertActorsInput, GetAlertActorsOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Alerts
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from komand_rapid7_insightidr.util.util import get_logging_context


class GetAlertActors(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_alert_actors",
            description=Component.DESCRIPTION,
            input=GetAlertActorsInput(),
            output=GetAlertActorsOutput(),
        )

    def run(self, params={}):
        alert_rrn = params.get(Input.ALERT_RRN)
        self.connection.session.headers["Accept-version"] = "strong-force-preview"
        request = ResourceHelper(self.connection.session, self.logger)
        params = {"size": params.get(Input.SIZE), "index": params.get(Input.INDEX)}
        self.logger.info(f"Getting the alert actors for {alert_rrn}...", **self.connection.log_values)
        response = request.make_request(
            Alerts.get_alert_actor(self.connection.url, alert_rrn), method="get", params=params
        )
        return {Output.ACTORS: response.get("actors", []), Output.METADATA: response.get("metadata", {})}
