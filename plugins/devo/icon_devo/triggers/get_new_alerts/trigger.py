import insightconnect_plugin_runtime
import time
from .schema import GetNewAlertsInput, GetNewAlertsOutput, Input, Output, Component
import datetime

# Custom imports below


class GetNewAlerts(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_new_alerts",
            description=Component.DESCRIPTION,
            input=GetNewAlertsInput(),
            output=GetNewAlertsOutput(),
        )

    def run(self, params={}):
        interval = params.get(Input.INTERVAL, 10)
        now = datetime.datetime.now()

        while True:
            time_ago = now - datetime.timedelta(seconds=interval)
            now = datetime.datetime.now()

            query = "from siem.logtrust.alert.info select *"

            new_alerts_query_output = self.connection.api.query(query, time_ago.isoformat(), now.isoformat())
            new_alerts = new_alerts_query_output.get("object", {})
            if new_alerts:
                self.logger.info("Alerts received, sending...")
                cleaned_result = insightconnect_plugin_runtime.helper.clean(new_alerts)
                self.send({Output.ALERTS: cleaned_result})
            else:
                self.logger.info("No new alerts found.")

            self.logger.info(f"Sleeping for {interval} seconds.\n")
            time.sleep(interval)
