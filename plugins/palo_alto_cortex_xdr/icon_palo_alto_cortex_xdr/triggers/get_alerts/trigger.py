import insightconnect_plugin_runtime
import time

from .schema import GetAlertsInput, GetAlertsOutput, Input, Output, Component

# Custom imports below

from ...util.util import Util


class GetAlerts(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_alerts", description=Component.DESCRIPTION, input=GetAlertsInput(), output=GetAlertsOutput()
        )

    def run(self, params={}):
        # For the Alerts API, you filter alerts by `creation_time` when requesting data, however the timestamp field in
        # the returned Alerts is `detection_time`
        alert_timestamp_field = "detection_timestamp"

        end_time = Util.now_ms()
        # Request all events between 1ms ago and now on first iteration.
        start_time = end_time - 1
        last_event_processed_time_ms = start_time

        self.logger.info("Initializing Get Alerts trigger for the Palo Alto Cortex XDR plugin.")

        while True:
            alerts = self.connection.xdr_api.get_alerts(from_time=start_time, to_time=end_time)

            for alert_time in Util.send_items_to_platform_for_trigger(
                self, alerts, Output.ALERT, last_event_processed_time_ms, alert_timestamp_field
            ):
                last_event_processed_time_ms = alert_time

            # Back off before next iteration
            time.sleep(params.get(Input.FREQUENCY, 5))

            # Update the start and end times for the next iteration. Don't request events older than our
            # last_processed_time_ms and set the end_time for the request to now.
            start_time = last_event_processed_time_ms
            end_time = Util.now_ms()
