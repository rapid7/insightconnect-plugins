import insightconnect_plugin_runtime
import time

from .schema import GetAlertsInput, GetAlertsOutput, Input, Output, Component

# Custom imports below

from ...util.util import Util


class GetAlerts(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_alerts',
                description=Component.DESCRIPTION,
                input=GetAlertsInput(),
                output=GetAlertsOutput()
        )

    def run(self, params={}):
        time_field = "creation_time"

        # Request all Alerts from one hour ago to now.
        one_hour_in_ms = 60 * 60 * 1000
        end_time = Util.now_ms()
        start_time = end_time - one_hour_in_ms
        last_event_processed_time_ms = start_time

        self.logger.info(f"Initializing Get Alerts trigger for the Palo Alto Cortex XDR plugin.")

        while True:
            alerts = self.connection.xdr_api.get_alerts(
                from_time=start_time, to_time=end_time, time_field=time_field
            )

            # Process alerts from oldest to newest
            for alert in alerts:
                alert_time = alert.get(time_field, -1)
                if alert_time > last_event_processed_time_ms:
                    last_event_processed_time_ms = alert_time
                    self.send({Output.ALERT: alert})

            # Back off before next iteration
            time.sleep(params.get("interval", 5))

            # Update the start and end times for the next iteration. Don't request events older than our
            # last_processed_time_ms and set the end_time for the request to now.
            start_time = last_event_processed_time_ms
            end_time = Util.now_ms()
