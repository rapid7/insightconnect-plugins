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
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        from_date = params.get(Input.FROM_DATE)
        # END INPUT BINDING - DO NOT REMOVE

        alerts = self.connection.client.get_all_alerts(since=from_date)

        for alert in alerts:
            alert["severity"] = alert.get("severity", "").upper()

        return {Output.ALERTS: alerts}
