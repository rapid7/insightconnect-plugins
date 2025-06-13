import insightconnect_plugin_runtime
import time
from .schema import GetNewAlertsInput, GetNewAlertsOutput, Input, Output, Component

# Custom imports below
import datetime
import json
from insightconnect_plugin_runtime.helper import clean
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightidr.util.endpoints import Alerts
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from komand_rapid7_insightidr.util.constants import TOTAL_SIZE
from komand_rapid7_insightidr.util.util import get_logging_context


class GetNewAlerts(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_new_alerts",
            description=Component.DESCRIPTION,
            input=GetNewAlertsInput(),
            output=GetNewAlertsOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        input_frequency = params.get(Input.FREQUENCY, 15)
        # END INPUT BINDING - DO NOT REMOVE
        self.logger.info("Get Alerts: trigger started", **self.connection.log_values)

        # Set initial set for storing initial alert_rrn values
        initial_alerts = set()

        # Flag to track the first execution
        first_execution = True

        while True:
            start_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=20)

            search = clean(
                {
                    "start_time": start_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "leql": params.get(Input.LEQL),
                    "terms": params.get(Input.TERMS),
                }
            )
            data = clean(
                {
                    "search": search,
                    "field_ids": params.get(Input.FIELD_IDS),
                    "aggregates": params.get(Input.AGGREGATES),
                }
            )

            result = self.make_resource_request(data)

            total_items = result.get("metadata", {}).get("total_items", 0)

            alerts = result.get("alerts", [])

            # If there are more than 100 results fetch more until all results are stored.
            if total_items > TOTAL_SIZE:
                index = TOTAL_SIZE
                while index < total_items:
                    data["search"]["index"] = index
                    result = self.make_resource_request(data)
                    alerts.extend(result.get("alerts", []))
                    index += 100

            # If not the first iteration send new alerts to output and create new list to compare on next fetch
            if not first_execution:
                for alert in alerts:
                    alert_rrn = alert["rrn"]
                    if alert_rrn not in initial_alerts:
                        self.send_alert(alert)
                initial_alerts = set(alert["rrn"] for alert in alerts)
            # For first iteration store alert_rrn's for last 20 minutes for comparison on next fetch.
            else:
                initial_alerts.update(alert["rrn"] for alert in alerts)
                first_execution = False

            # Back off before next iteration (sleep for 15 seconds)
            time.sleep(input_frequency)

    def make_resource_request(self, data):
        try:
            self.connection.session.headers["Accept-version"] = "strong-force-preview"
            request = ResourceHelper(self.connection.session, self.logger)
            endpoint = Alerts.get_alert_serach(self.connection.url)
            response = request.resource_request(endpoint, "post", payload=data)
            return self.parse_json_response(response)
        except Exception as error:
            raise PluginException(
                cause="Error: Failed to retrieve alert results.", assistance=f"Exception returned was {error}"
            )

    def parse_json_response(self, response):
        try:
            return json.loads(response.get("resource", {}))
        except Exception as error:
            raise PluginException(
                cause="Error: Failed to process alert results.", assistance=f"Exception returned was {error}"
            )

    def send_alert(self, alert: dict):
        self.logger.info(f"Alert found: {alert.get('rrn')}", **self.connection.log_values)
        self.send({Output.ALERT: clean(alert)})
