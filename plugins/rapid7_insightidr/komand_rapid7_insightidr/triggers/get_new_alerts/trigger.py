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
MAX_LOOKBACK_HOURS = 24
MAX_NUMBER_OF_RETRIES = 20
RETRY_DELAY_SECONDS = 30

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
            current_time = self.get_current_time()

            # Look back from the last successful poll so alerts created during an outage are not missed
            window_end = datetime.datetime.fromisoformat(last_poll_iso) if last_poll_iso else current_time

            # Set the start time based on the window end time and lookback window
            lookback_start = window_end - datetime.timedelta(minutes=LOOKBACK_MINUTES)
            lookback_floor = current_time - datetime.timedelta(hours=MAX_LOOKBACK_HOURS)

            # If the lookback start is before the floor, set the start time to the floor
            if lookback_start < lookback_floor:
                self.logger.info(
                    f"Get Alerts: last poll {last_poll_iso} is older than {MAX_LOOKBACK_HOURS} hours, alerts created before {lookback_floor.isoformat()} are skipped"
                )
            start_time = max(lookback_start, lookback_floor)

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

            # In case of any errors, log the error, wait for the retry delay, and retry
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
                    f"The request will be retried after {RETRY_DELAY_SECONDS} seconds... ({retry_attempts_counter}/{MAX_NUMBER_OF_RETRIES})"
                )
                time.sleep(RETRY_DELAY_SECONDS)
                continue

            # Send new alerts and collect the RRNs from this poll
            latest_alerts = self.process_alerts(alerts, initial_alerts, first_execution)

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
        # The API only returns full alerts within the first 100 results (index + 1) * size <= 100
        # This is a workaround to get all alerts by using a sort and pagination
        data = {**data, "sorts": [{"field_id": "alert.created_at", "order": "ASCENDING_NULLS_LAST"}]}
        alerts = []
        while True:
            # Get the alerts and add to the list of alerts
            page = self.make_resource_request(data).get("alerts", [])
            alerts.extend(page)

            # Get the last alert timestamp
            next_start = page[-1].get("created_at") if len(page) >= TOTAL_SIZE else None

            # If no more results, we've got them all
            if not next_start:
                if len(page) >= TOTAL_SIZE:
                    self.logger.info("Get Alerts: last alert on a full page has no created_at, stopping paging")
                return alerts

            # Compare instants, not strings: the first start_time has no milliseconds but created_at does
            start_time = datetime.datetime.fromisoformat(data.get("search", {}).get("start_time"))
            next_time = datetime.datetime.fromisoformat(next_start)

            # If the next start time is before the start time, we've hit a stall and should stop paging
            if next_time < start_time:
                self.logger.info(f"Get Alerts: paging stalled at {next_start}, skipping the rest of the alerts")
                return alerts

            # Prevent infinite loop if multiple alerts were created in the same millisecond
            if next_time == start_time:
                # Just to ensure we don't get stuck in a loop
                self.logger.info(
                    f"Get Alerts: more than {TOTAL_SIZE} alerts created at {next_start}, skipping the rest of them"
                )
                next_time += datetime.timedelta(milliseconds=1)
                next_start = (
                    next_time.astimezone(datetime.UTC).isoformat(timespec="milliseconds").replace("+00:00", "Z")
                )

            # Update the start time for the next iteration
            data = {**data, "search": {**data.get("search", {}), "start_time": next_start}}

    def make_resource_request(self, data: dict[str, Any]) -> dict[str, Any]:
        try:
            self.connection.headers["Accept-version"] = "strong-force-preview"
            request = ResourceHelper(self.connection.headers, self.logger)
            endpoint = Alerts.get_alert_serach(self.connection.url)
            response = request.resource_request(endpoint, "post", payload=data, params={"size": TOTAL_SIZE})
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

    def process_alerts(self, alerts: list[dict[str, Any]], initial_alerts: set[str], first_execution: bool) -> set[str]:
        latest_alerts = set()
        for index, alert in enumerate(alerts):
            # Skip alerts without an RRN, we can't track them between polls
            if not (alert_rrn := alert.get("rrn")):
                self.logger.info(f"Alert {index}: does not have an RRN, skipping this alert.")
                continue

            # The same alert can be returned on several pages of one poll, send it only once
            if alert_rrn in latest_alerts:
                continue
            latest_alerts.add(alert_rrn)

            # If not the first iteration send new alerts to output
            # For first iteration only store alert_rrn's for comparison on next fetch
            if not first_execution and alert_rrn not in initial_alerts:
                self.send_alert(alert)

        # Return the RRNs to compare against on the next poll
        return latest_alerts

    def send_alert(self, alert: dict[str, Any]) -> None:
        self.logger.info(f"Alert found: {alert.get('rrn')}")
        self.send({Output.ALERT: clean(alert)})

    @staticmethod
    def get_current_time() -> datetime.datetime:
        return datetime.datetime.now(datetime.UTC)
