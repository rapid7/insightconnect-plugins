import insightconnect_plugin_runtime
import time
from datetime import datetime
from .schema import PollAlertListInput, PollAlertListOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import json


class PollAlertList(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="poll_alert_list",
            description=Component.DESCRIPTION,
            input=PollAlertListInput(),
            output=PollAlertListOutput(),
        )

    def run(self, params={}):
        """Run the trigger"""
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        start_date_time = params.get(Input.START_DATE_TIME)
        end_date_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")  # Current time in UTC

        while True:
            new_alerts = []
            # Make Action API Call
            self.logger.info("Making API Call...")
            try:
                client.consume_alert_list(
                    lambda alert: new_alerts.append(alert.json()),
                    start_time=start_date_time,
                    end_time=end_date_time,
                )
            except Exception as error:
                raise PluginException(
                    cause="An error occurred while polling alerts.",
                    assistance="Please check your inputs and try again.",
                    data=error,
                )
            # Load json objects to list
            alert_list = []
            for new_alert in new_alerts:
                alert_list.append(json.loads(new_alert))
            # Return results
            self.logger.info("Returning Results...")
            self.send({Output.TOTAL_COUNT: len(new_alerts), Output.ALERTS: alert_list})
            # Sleep before next run
            time.sleep(params.get(Input.INTERVAL, 1800))
            # Update start_date_time and end_date_time for the next iteration
            start_date_time = end_date_time
            end_date_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")  # Current time in UTC
