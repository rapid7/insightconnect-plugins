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
            response = client.alert.consume(
                lambda alert: new_alerts.append(json.loads(alert.model_dump_json())),
                start_time=start_date_time,
                end_time=end_date_time,
            )
            if "error" in response.result_code.lower():
                raise PluginException(
                    cause="An error occurred while polling alerts.",
                    assistance="Please check your inputs and try again.",
                    data=response.error,
                )
            # Return results
            self.logger.info("Returning Results...")
            self.send({Output.TOTAL_COUNT: len(new_alerts), Output.ALERTS: new_alerts})
            # Sleep before next run
            time.sleep(params.get(Input.INTERVAL, 1800))
            # Update start_date_time and end_date_time for the next iteration
            start_date_time = end_date_time
            end_date_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")  # Current time in UTC
