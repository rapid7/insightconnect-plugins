import insightconnect_plugin_runtime
import time

from .schema import GetIncidentsInput, GetIncidentsOutput, Input, Output, Component

# Custom imports below

from ...util.util import Util


class GetIncidents(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_incidents",
            description=Component.DESCRIPTION,
            input=GetIncidentsInput(),
            output=GetIncidentsOutput(),
        )

    def run(self, params={}):
        time_field = "creation_time"

        # We will be asking for incidents between one hour ago and now.
        one_hour_in_ms = 60 * 60 * 1000
        end_time = Util.now_ms()
        start_time = end_time - one_hour_in_ms
        last_event_processed_time_ms = start_time

        self.logger.info(f"Initializing Get Incidents trigger for the Palo Alto Cortex XDR plugin.")

        while True:
            # incidents = self.connection.xdr_api.get_incidents(
            #     from_time=start_time, to_time=end_time, time_field=time_field
            # )

            incidents = [{time_field: 1577024425126}, {time_field: 1577024425127}, {time_field: 1577024425128}, {time_field: 1577024425129}, {time_field: 1577024425130}]

            # Process incidents from oldest to newest
            for incident_time in Util.send_items_to_platform_for_trigger(
                    self, incidents, Output.INCIDENT, last_event_processed_time_ms
            ):
                last_event_processed_time_ms = incident_time

            # Back off before next iteration
            time.sleep(params.get("interval", 5))

            # Update the start and end times for the next iteration. Don't request events older than our
            # last_processed_time_ms and set the end_time for the request to now.
            start_time = last_event_processed_time_ms
            end_time = Util.now_ms()


if __name__ == "__main__":
    trigger = GetIncidents()
    trigger.run()
