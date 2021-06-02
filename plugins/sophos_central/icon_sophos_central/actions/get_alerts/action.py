import insightconnect_plugin_runtime
from .schema import GetAlertsInput, GetAlertsOutput, Input, Output, Component

# Custom imports below


class GetAlerts(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_alerts",
            description=Component.DESCRIPTION,
            input=GetAlertsInput(),
            output=GetAlertsOutput(),
        )

    def run(self, params={}):
        alerts_response = self.connection.client.get_alerts(since=params.get(Input.FROM_DATE))
        alerts = alerts_response.get("items", [])
        for i in range(999):
            if not alerts_response.get("has_more"):
                break

            alerts_response = self.connection.client.get_alerts(key=alerts_response.get("pages", {}).get("nextKey"))
            alerts.extend(alerts_response.get("items"))

        for alert in alerts:
            alert["severity"] = alert["severity"].upper()

        return {Output.ALERTS: alerts}
