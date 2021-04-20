import insightconnect_plugin_runtime
import time
from .schema import GetNewAlertsInput, GetNewAlertsOutput, Input, Output, Component

# Custom imports below
from komand_recorded_future.util.api import Endpoint
from datetime import datetime


class GetNewAlerts(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_new_alerts",
            description=Component.DESCRIPTION,
            input=GetNewAlertsInput(),
            output=GetNewAlertsOutput(),
        )

    def run(self, params={}):
        interval = params.get(Input.FREQUENCY)
        now = datetime.now()

        while True:
            then = now
            now = datetime.now()

            # triggered = [2017 - 07 - 30,)
            # // same as 7 / 30 / 2017 <= triggered
            params = {"triggered": f"[{then.isoformat()},]"}
            alerts = insightconnect_plugin_runtime.helper.clean(
                self.connection.client.make_request(Endpoint.search_alerts(), params).get("data").get("results")
            )

            for alert in alerts:
                self.send({Output.ALERT: alert})
            else:
                self.logger.info("No new alerts found.")

            self.logger.info(f"Sleeping for {interval}")
            time.sleep(interval)
