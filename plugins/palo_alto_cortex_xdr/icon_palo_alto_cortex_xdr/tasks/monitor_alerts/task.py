import insightconnect_plugin_runtime
from requests import Response

from .schema import (
    MonitorAlertsInput,
    MonitorAlertsOutput,
    MonitorAlertsState,
    Component,
)
from datetime import datetime, timedelta, timezone
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import hash_sha1
from typing import Any, Dict, Tuple, Union, List

TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
MAX_LOOKBACK_DAYS = 7
DEFAULT_LOOKBACK_HOURS = 24
# This is the max amount of alerts that can be returned by the API in search from -> search_to
ALERT_LIMIT = 100

# State held values
LAST_ALERT_TIME = "last_alert_time"
LAST_ALERT_HASH = "last_alert_hash"
LAST_QUERY_TIME = "last_query_time"
TOTAL_COUNT = "total_count"
CURRENT_COUNT = "current_count"

# State held values for paging through results
SEARCH_START_TIME = "start_time"
SEARCH_END_TIME = "end_time"

# General [agination
LAST_SEARCH_FROM = "last_search_from"
LAST_SEARCH_TO = "last_search_to"
TIMESTAMP_KEY = "detection_timestamp"


class MonitorAlerts(insightconnect_plugin_runtime.Task):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_alerts",
            description=Component.DESCRIPTION,
            input=MonitorAlertsInput(),
            output=MonitorAlertsOutput(),
            state=MonitorAlertsState(),
        )
        self.time_sort_field = "creation_time"

    def run(self, params={}, state={}, custom_config: dict = {}):  # pylint: disable=unused-argument
        existing_state = state.copy()

        try:
            alert_limit = self.get_alert_limit(custom_config=custom_config)
            now_time = self._get_current_time()
            start_time = self._parse_custom_config(custom_config, now_time, existing_state)

            self.logger.info("Starting to download alerts...")

            response, state, has_more_pages = self.get_alerts_palo_alto(
                state=state, start_time=start_time, end_time=now_time, alert_limit=alert_limit
            )

            return response, state, has_more_pages, 200, None

        except PluginException as error:
            if isinstance(error.data, Response):
                # if there is response data in the error then use it in the exception
                status_code = error.data.status_code
                cause = error.data.text
            else:
                status_code = 500
                cause = error.cause

            self.logger.error(
                f"A PluginException has occurred. Status code {status_code} returned. Error: {cause}. "
                f"Existing state: {existing_state}"
            )
            return [], existing_state, False, status_code, PluginException(cause=cause, data=error)
        except Exception as error:
            self.logger.error(
                f"Unknown exception has occurred. No results returned. Error: {error} "
                f"Existing state: {existing_state}"
            )
            return [], existing_state, False, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    ###########################
    # Make request
    ###########################
    def get_alerts_palo_alto(self, state: dict, start_time: int, end_time: int, alert_limit: int):
        """ """

        search_from = state.get(LAST_SEARCH_TO, 0)

        search_to = search_from + alert_limit

        filters = []

        # If time constraints have been provided for the request, add them to the post body
        if start_time is not None and end_time is not None:
            filters.append({"field": self.time_sort_field, "operator": "gte", "value": start_time})
            filters.append({"field": self.time_sort_field, "operator": "lte", "value": end_time})

        post_body = self.build_post_body(search_from=search_from, search_to=search_to, filters=filters)

        results, results_count, total_count = self.connection.xdr_api.get_response_alerts(post_body)

        state[TOTAL_COUNT] = total_count
        state[CURRENT_COUNT] = state.get(CURRENT_COUNT, 0) + results_count

        new_alerts, last_alert_hashes, last_alert_time = self._dedupe_and_get_highest_time(results, start_time, state)

        is_paginating = state.get(CURRENT_COUNT, 0) != state.get(TOTAL_COUNT)

        has_more_pages = False

        if is_paginating:
            has_more_pages = True
            self.logger.info(f"Found total alerts={total_count}, limit={alert_limit}, is_paginating={is_paginating}")
            self.logger.info(
                f"Paginating alerts: Saving state with existing filters: "
                f"search_from = {search_from} "
                f"search_to = {search_to} "
                f"current_count = {state.get(CURRENT_COUNT)} "
                f"total_count = {state.get(TOTAL_COUNT)}"
            )
            state[LAST_SEARCH_TO] = search_to
            state[LAST_QUERY_TIME] = start_time
            state[LAST_SEARCH_FROM] = search_from
            state[SEARCH_START_TIME] = start_time
            state[SEARCH_END_TIME] = end_time
        else:
            state = self._drop_pagination_state(state)
            self.logger.info(f"Remaining alerts: {len(new_alerts)}, is_paginating: {is_paginating}, \nstate: {state}")
            has_more_pages = False
            # return new_alerts, state, has_more_pages

        # add the last alert time to the state if it exists
        # if not then set to the last queried time to move the filter forward
        state[LAST_ALERT_TIME] = last_alert_time if last_alert_time else end_time
        # update hashes in state only if we've got new ones
        state[LAST_ALERT_HASH] = last_alert_hashes if last_alert_hashes else state.get(LAST_ALERT_HASH, [])

        return new_alerts, state, has_more_pages

    ###########################
    # Deduping
    ###########################
    def _dedupe_and_get_highest_time(self, alerts: list, start_time: int, state: dict) -> Tuple[list, list, str]:
        """
        Function to dedupe alerts using existing hashes in the state, and return the highest
        timestamp.

        :param alerts: list of alerts
        :param state: state of the plugin
        :return: list of deduped alerts, list of new hashes, and the highest timestamp
        """

        old_hashes, deduped_alerts, new_hashes, highest_timestamp = state.get(LAST_ALERT_HASH, []), [], [], ""
        for index, alert in enumerate(alerts):
            alert_time = alert.get(TIMESTAMP_KEY)
            if alert_time == start_time:
                alert_hash = hash_sha1(alert)
                if alert_hash not in old_hashes:
                    deduped_alerts.append(alert)
            elif alert_time > start_time:
                deduped_alerts += alerts[index:]
                break

        num_deduped_alerts = len(deduped_alerts)
        num_alerts = len(alerts)
        self.logger.info(f"Received {num_alerts} alerts, and after dedupe there is {num_deduped_alerts} results.")

        if deduped_alerts:
            # alert results are already sorted by CS API, so get the latest timestamp
            highest_timestamp = deduped_alerts[-1].get(TIMESTAMP_KEY)

            for alert in deduped_alerts:
                if alert.get(TIMESTAMP_KEY) == highest_timestamp:
                    new_hashes.append(hash_sha1(alert))
                    self.logger.info(f"Hashed latest event with timestamp {highest_timestamp}.")

            self.logger.debug(f"Highest timestamp is {highest_timestamp}")
            self.logger.debug(f"Last hash is {new_hashes}")

        return deduped_alerts, new_hashes, highest_timestamp

    @staticmethod
    def _get_current_time():
        # Gets the last 15 minutes in UNIX
        last_15_min = datetime.utcnow() - timedelta(minutes=15)
        return int(last_15_min.timestamp()) * 1000

    ###########################
    # Custom Config
    ###########################
    def _parse_custom_config(
        self, custom_config: Dict[str, Any], now: int, saved_state: Dict[int, str]
    ) -> Tuple[int, int]:
        """
        Takes custom config from CPS and allows the specification of a new start time for alerts,
        and allows the limit to be customised.

        :param custom_config: custom_config for the plugin
        :param now: datetime representing 'now'
        :param saved_state: existing state of the integration
        :return: string formatted time to apply to our alert queries, and limit integer to set how many
        alerts to fetch per run.
        """
        state = saved_state.copy()
        log_msg = ""
        first_run = True

        dt_now = self.convert_unix_to_datetime(now)

        # TODO - Fix this it's confusing
        saved_time = state.get(LAST_QUERY_TIME, state.get(LAST_ALERT_TIME))
        start_time = saved_state.get(SEARCH_START_TIME, saved_time)

        if not saved_time:
            log_msg += "No previous alert time within state. "
            custom_timings = custom_config.get(LAST_ALERT_TIME, {})
            custom_date = custom_timings.get("date")
            custom_hours = custom_timings.get("hours", DEFAULT_LOOKBACK_HOURS)
            start = datetime(**custom_date) if custom_date else (dt_now - timedelta(hours=custom_hours))
            state[LAST_ALERT_TIME] = start.strftime(TIME_FORMAT)
        else:
            first_run = False

            # check if we have held the TS beyond our max lookback
            lookback_days = custom_config.get(f"{LAST_ALERT_TIME}_days", MAX_LOOKBACK_DAYS)
            default_date_lookback = dt_now - timedelta(days=lookback_days)  # if not passed from CPS create on the fly

            custom_lookback = custom_config.get(f"max_{LAST_ALERT_TIME}", {})
            comparison_date = datetime(**custom_lookback) if custom_lookback else default_date_lookback
            comparison_date = comparison_date.replace(tzinfo=timezone.utc).strftime(TIME_FORMAT)
            comparison_date = self.convert_to_unix(comparison_date)

            if comparison_date > saved_time:
                self.logger.info(f"Saved time ({saved_time}) exceeds cut off, moving to ({comparison_date}).")
                state[LAST_ALERT_TIME] = comparison_date

        start_time = state.get(LAST_ALERT_TIME)
        self.logger.info(f"{log_msg}Applying the following start time='{start_time}'.")

        if first_run:
            start_time = self.convert_to_unix(start_time)
            state[SEARCH_START_TIME] = start_time

        return start_time

    ###########################
    # Build post body
    ###########################
    def build_post_body(
        self, search_from: int, search_to: int, filters: List[Dict[str, Union[str, int]]]
    ) -> Dict[str, Dict[str, Union[int, Dict[str, str], List[Dict[str, Union[str, int]]]]]]:
        """
        Helper method to build the post body for the request

        :param search_from: An integer representing the starting offset within the query result set from which you want alerts returned
        :param search_to: An integer representing the end offset within the result set after which you do not want alerts returned
        :param filters: An array of filter fields

        :return post_body:
        """
        post_body = {
            "request_data": {
                "search_from": search_from,
                "search_to": search_to,
                "sort": {"field": self.time_sort_field, "keyword": "asc"},
                "filters": filters,
            }
        }
        return post_body

    ###########################
    # Datetime Helpers
    ###########################
    def convert_unix_to_datetime(self, unix_time: int) -> datetime:
        return datetime.fromtimestamp(unix_time / 1000, tz=timezone.utc)

    def convert_to_unix(self, date_time: datetime) -> int:
        return int(datetime.strptime(date_time, TIME_FORMAT).timestamp()) * 1000

    def _drop_pagination_state(self, state: dict) -> Dict[str, Union[int, str, list]]:
        """
        Helper function to pop values from the state if we need to break out of pagination.

        :return: state
        """
        log_msg = "Dropped the following keys from state: "
        if state.get(LAST_SEARCH_FROM):
            log_msg += f"{LAST_SEARCH_FROM}; "
            state.pop(LAST_SEARCH_FROM)

        if state.get(LAST_SEARCH_TO):
            log_msg += f"{LAST_SEARCH_TO}; "
            state.pop(LAST_SEARCH_TO)

        if state.get(TOTAL_COUNT):
            log_msg += f"{TOTAL_COUNT}; "
            state.pop(TOTAL_COUNT)

        if state.get(CURRENT_COUNT):
            log_msg += f"{CURRENT_COUNT}; "
            state.pop(CURRENT_COUNT)

        if state.get(LAST_QUERY_TIME):
            log_msg += f"{LAST_QUERY_TIME}; "
            state.pop(LAST_QUERY_TIME)

        if state.get(SEARCH_START_TIME):
            log_msg += f"{SEARCH_START_TIME}; "
            state.pop(SEARCH_START_TIME)

        if state.get(SEARCH_END_TIME):
            log_msg += f"{SEARCH_END_TIME}; "
            state.pop(SEARCH_END_TIME)

        self.logger.debug(log_msg)

        return state

    def get_alert_limit(self, custom_config: dict) -> int:
        """ """

        # set the alert limit from CPS if it exists, otherwise default to ALERT_LIMIT
        # Safety check if user tries to make search greater than 100
        alert_limit = custom_config.get("alert_limit", ALERT_LIMIT)

        if alert_limit > ALERT_LIMIT:
            self.logger.info(f"Alert limit exceeds {ALERT_LIMIT}, falling back to {ALERT_LIMIT}")
            alert_limit = ALERT_LIMIT

        return alert_limit
