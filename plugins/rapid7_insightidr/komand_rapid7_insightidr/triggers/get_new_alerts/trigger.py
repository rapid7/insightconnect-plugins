import insightconnect_plugin_runtime
import time
from .schema import GetNewAlertsInput, GetNewAlertsOutput, Input, Output, Component

# Custom imports below
import datetime
import json
from typing import Any
from insightconnect_plugin_runtime.helper import clean
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightidr.util.endpoints import Alerts
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from komand_rapid7_insightidr.util.constants import TOTAL_SIZE

LOOKBACK_MINUTES = 20
MAX_NUMBER_OF_RETRIES = 20

STATE_KEY = "RRNs"
TIME_STATE_KEY = "last_poll_time"


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
        input_leql = params.get(Input.LEQL)
        input_terms = params.get(Input.TERMS)
        input_field_ids = params.get(Input.FIELD_IDS)
        input_aggregates = params.get(Input.AGGREGATES)
        # END INPUT BINDING - DO NOT REMOVE
        self.logger.info("Get Alerts: trigger started")

        # Restore alert_rrn values from state
        retry_attempts_counter, initial_alerts = 0, set(self.state.get(STATE_KEY, []))

        # Flag to track the first execution (skipped in case of resuming from a persisted state)
        first_execution = STATE_KEY not in self.state
        if last_poll_iso := self.state.get(TIME_STATE_KEY):
            self.logger.info(f"Detected a container restart, resuming from last poll time: {last_poll_iso}")

        while True:
            # Set the time for the current iteration
            current_time = datetime.datetime.now(datetime.UTC)

            # Look back from the last successful poll so alerts created during an outage are not missed
            window_end = datetime.datetime.fromisoformat(last_poll_iso) if last_poll_iso else current_time
            start_time = window_end - datetime.timedelta(minutes=LOOKBACK_MINUTES)

            # Prepare the request data
            search = clean(
                {
                    "start_time": start_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "leql": input_leql,
                    "terms": input_terms,
                }
            )
            data = clean(
                {
                    "search": search,
                    "field_ids": input_field_ids,
                    "aggregates": input_aggregates,
                }
            )

            # In case of any errors, log the error, wait for the defined frequency, and retry
            try:
                alerts = self.get_alerts(data)
            except Exception as error:
                # If max retries reached, raise the error
                if retry_attempts_counter >= MAX_NUMBER_OF_RETRIES:
                    raise PluginException(
                        cause=f"Failed to retrieve alerts after {MAX_NUMBER_OF_RETRIES} retries.",
                        assistance="Please verify the connection to InsightIDR and try again. If the issue persists, please contact support.",
                        data=error,
                    )

                # Otherwise, log the error and retry after waiting
                retry_attempts_counter += 1
                self.logger.error("Get Alerts: An error occurred while fetching alerts")
                self.logger.error(error)
                self.logger.info(
                    f"The request will be retried after {input_frequency} seconds... ({retry_attempts_counter}/{MAX_NUMBER_OF_RETRIES})"
                )
                time.sleep(input_frequency)
                continue

            latest_alerts = set()
            for index, alert in enumerate(alerts):
                if not (alert_rrn := alert.get("rrn")):
                    self.logger.info(f"Alert {index}: does not have an RRN, skipping this alert.")
                    continue
                latest_alerts.add(alert_rrn)

                # If not the first iteration send new alerts to output
                # For first iteration only store alert_rrn's for comparison on next fetch
                if not first_execution and alert_rrn not in initial_alerts:
                    self.send_alert(alert)

            # Update the stored alert_rrn's and reset the retry counter
            initial_alerts, first_execution = latest_alerts, False
            last_poll_iso, retry_attempts_counter = current_time.isoformat(), 0

            # Save the state for fallback in case of plugin restart (only possible when a trigger ID is provided)
            if self.state_file:
                self.state[TIME_STATE_KEY] = last_poll_iso  # we need to save this as a string
                self.state[STATE_KEY] = list(initial_alerts)
                self._save_state()

            # Back off before next iteration
            self.logger.info(f"Sleeping for {input_frequency} seconds...")
            time.sleep(input_frequency)

    def get_alerts(self, data: dict[str, Any]) -> list[dict[str, Any]]:
        # Fetch the first batch of alerts
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
                index += TOTAL_SIZE
        return alerts

    def make_resource_request(self, data: dict[str, Any]) -> dict[str, Any]:
        try:
            self.connection.headers["Accept-version"] = "strong-force-preview"
            request = ResourceHelper(self.connection.headers, self.logger)
            endpoint = Alerts.get_alert_serach(self.connection.url)
            response = request.resource_request(endpoint, "post", payload=data)
            return self.parse_json_response(response)
        except Exception as error:
            raise PluginException(
                cause="Error: Failed to retrieve alert results.", assistance=f"Exception returned was {error}"
            )

    def parse_json_response(self, response: dict[str, Any]) -> dict[str, Any]:
        try:
            return json.loads(response.get("resource", {}))
        except Exception as error:
            raise PluginException(
                cause="Error: Failed to process alert results.", assistance=f"Exception returned was {error}"
            )

    def send_alert(self, alert: dict[str, Any]) -> None:
        self.logger.info(f"Alert found: {alert.get('rrn')}")
        self.send({Output.ALERT: clean(alert)})
