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
from typing import Any, Dict, Tuple, Union, Optional

TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
MAX_LOOKBACK_DAYS = 7
DEFAULT_LOOKBACK_HOURS = 24
# This is the max amount of alerts that can be returned by the API in search from -> search_to
ALERT_LIMIT = 100

# State held values
LAST_ALERT_TIME = "last_alert_time"
LAST_ALERT_HASH = "last_alert_hash"
CURRENT_COUNT = "current_count"

# State held values for paging through results
QUERY_START_TIME = "query_start_time"
QUERY_END_TIME = "query_end_time"

# General Pagination
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

        custom_config = {
            "last_alert_time": {
                "date": {"year": 2024, "month": 8, "day": 1, "hour": 1, "minute": 2, "second": 3, "microsecond": 0}
            },
            "max_last_alert_time": {
                "year": 2024,
                "month": 8,
                "day": 2,
                "hour": 3,
                "minute": 4,
                "second": 5,
                "microsecond": 0,
            },
            "alert_limit": 100,
        }
        try:
            alert_limit = self.get_alert_limit(custom_config=custom_config)
            now_time = self._get_current_time()
            start_time = self._parse_custom_config(custom_config, now_time, existing_state)

            self.logger.info("Starting to download alerts...")

            response, state, has_more_pages = self.get_alerts_palo_alto(
                state=state, start_time=start_time, now=now_time, alert_limit=alert_limit
            )

            return response, state, has_more_pages, 200, None

        except PluginException as error:
            if isinstance(error.data, Response):
                # if there is response data in the error then use it in the exception
                status_code = error.data.status_code
            else:
                status_code = 500

            self.logger.error(
                f"A PluginException has occurred. Status code {status_code} returned. Error: {error}. "
                f"Existing state: {existing_state}"
            )
            return [], existing_state, False, status_code, PluginException(data=error)

        except Exception as error:
            self.logger.error(
                f"Unknown exception has occurred. No results returned. Error: {error} "
                f"Existing state: {existing_state}"
            )

            return (
                [],
                existing_state,
                False,
                500,
                PluginException(preset=PluginException.Preset.UNKNOWN, data=error),
            )

    ###########################
    # Make request
    ###########################
    def get_alerts_palo_alto(self, state: dict, start_time: Optional[int], now: int, alert_limit: int):
        """ """

        query_start_time = state.get(QUERY_START_TIME, start_time)
        query_end_time = state.get(QUERY_END_TIME, now)

        search_from = state.get(LAST_SEARCH_TO, 0)
        search_to = search_from + alert_limit

        post_body = self.build_post_body(
            search_from=search_from, search_to=search_to, start_time=query_start_time, end_time=query_end_time
        )

        results, results_count, total_count = self.connection.xdr_api.get_response_alerts(post_body)

        state[CURRENT_COUNT] = state.get(CURRENT_COUNT, 0) + results_count

        new_alerts, new_alert_hashes, last_alert_time = self._dedupe_and_get_highest_time(results, start_time, state)

        is_paginating = state.get(CURRENT_COUNT) < total_count

        if is_paginating:
            self.logger.info(f"Found total alerts={total_count}, limit={alert_limit}, is_paginating={is_paginating}")
            self.logger.info(
                f"Paginating alerts: Saving state with existing filters: "
                f"search_from = {search_from} "
                f"search_to = {search_to} "
                f"current_count = {state.get(CURRENT_COUNT)} "
                f"total_count = {total_count}"
            )
            state[LAST_SEARCH_TO] = search_to
            state[LAST_SEARCH_FROM] = search_from
            state[QUERY_START_TIME] = query_start_time
            state[QUERY_END_TIME] = query_end_time
        else:
            self.logger.info(
                f"Paginating final page of alerts: "
                f"search_from = {search_from} "
                f"search_to = {search_to} "
                f"current_count = {state.get(CURRENT_COUNT)} "
                f"total_count = {total_count} "
            )
            state = self._drop_pagination_state(state)

        # add the last alert time to the state if it exists
        # if not then set to the last queried time to move the filter forward
        state[LAST_ALERT_TIME] = last_alert_time if last_alert_time else now
        # update hashes in state only if we've got new ones
        state[LAST_ALERT_HASH] = new_alert_hashes if new_alert_hashes else state.get(LAST_ALERT_HASH, [])

        return new_alerts, state, is_paginating

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

        self.logger.info(f"Received {len(alerts)} alerts, and after dedupe there is {len(deduped_alerts)} results.")

        if deduped_alerts:
            # alert results are already sorted by CS API, so get the latest timestamp
            highest_timestamp = deduped_alerts[-1].get(TIMESTAMP_KEY)

            for alert in deduped_alerts:
                if alert.get(TIMESTAMP_KEY) == highest_timestamp:
                    new_hashes.append(hash_sha1(alert))

            self.logger.debug(f"Highest timestamp is {highest_timestamp}")
            self.logger.debug(f"Last hash is {new_hashes}")

        return deduped_alerts, new_hashes, highest_timestamp

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

        end_time = state.get(QUERY_END_TIME, now)
        dt_now = self.convert_unix_to_datetime(end_time)

        saved_time = state.get(QUERY_START_TIME, state.get(LAST_ALERT_TIME))

        if not saved_time:
            log_msg += "No previous alert time within state.\n"
            custom_timings = custom_config.get(LAST_ALERT_TIME, {})
            custom_date = custom_timings.get("date")
            custom_hours = custom_timings.get("hours", DEFAULT_LOOKBACK_HOURS)
            start = datetime(**custom_date) if custom_date else (dt_now - timedelta(hours=custom_hours))
            state[LAST_ALERT_TIME] = self.convert_datetime_to_unix(start)
        else:
            # check if we have held the TS beyond our max lookback
            lookback_days = custom_config.get(f"{LAST_ALERT_TIME}_days", MAX_LOOKBACK_DAYS)
            default_date_lookback = dt_now - timedelta(days=lookback_days)  # if not passed from CPS create on the fly
            custom_lookback = custom_config.get(f"max_{LAST_ALERT_TIME}", {})
            comparison_date = datetime(**custom_lookback) if custom_lookback else default_date_lookback

            comparison_unix = self.convert_datetime_to_unix(comparison_date)

            # Update state if saved time exceeds the lookback limit
            if comparison_unix > saved_time:
                saved_time_str = self.convert_timestamp_to_string(saved_time)
                comparison_str = self.convert_timestamp_to_string(comparison_unix)
                self.logger.info(f"Saved time {saved_time_str} exceeds cut off, moving to {comparison_str}.")
                state[LAST_ALERT_TIME] = comparison_unix

                # Reset the offsets when changing search timer
                state[LAST_SEARCH_FROM] = 0
                state.pop(LAST_SEARCH_TO, None)

                # Reset the end time / default to now
                state[QUERY_END_TIME] = now

        start_time = state.get(LAST_ALERT_TIME)
        state[QUERY_START_TIME] = state.get(LAST_ALERT_TIME)

        self.logger.info(
            f"{log_msg}Applying the following start time='{self.convert_timestamp_to_string(start_time)}'."
        )

        return start_time

    ###########################
    # Build post body
    ###########################
    def build_post_body(self, search_from: int, search_to: int, start_time: int, end_time: int) -> dict:
        """
        Helper method to build the post body for the request

        :param search_from: An integer representing the starting offset within the query result set from which you want alerts returned
        :param search_to: An integer representing the end offset within the result set after which you do not want alerts returned
        :param filters: An array of filter fields

        :return post_body:
        """
        filters = [
            {"field": self.time_sort_field, "operator": "gte", "value": start_time},
            {"field": self.time_sort_field, "operator": "lte", "value": end_time},
        ]

        self.logger.info(
            f"Query start time: {self.convert_timestamp_to_string(start_time)}, Query end time: {self.convert_timestamp_to_string(end_time)}"
        )

        post_body = {
            "request_data": {
                "search_from": search_from,
                "search_to": search_to,
                "sort": {"field": self.time_sort_field, "keyword": "asc"},
                "filters": filters,
            }
        }

        self.logger.debug(f"Post Body: {post_body}")

        return post_body

    ###########################
    # Datetime Helpers
    ###########################
    def convert_unix_to_datetime(self, unix_time: int) -> datetime:
        return datetime.fromtimestamp(unix_time / 1000, tz=timezone.utc)

    def convert_datetime_to_unix(self, date_time: datetime) -> int:
        # Ensure the datetime object is in UTC
        if date_time.tzinfo is None:
            date_time = date_time.replace(tzinfo=timezone.utc)

        return int(date_time.timestamp() * 1000)

    def convert_timestamp_to_string(self, timestamp: int) -> str:
        return datetime.fromtimestamp(timestamp / 1000, tz=timezone.utc).strftime(TIME_FORMAT)

    @staticmethod
    def _get_current_time():
        # Gets the last 15 minutes in UNIX
        last_15_min = datetime.utcnow() - timedelta(minutes=15)
        return int(last_15_min.timestamp()) * 1000

    def _drop_pagination_state(self, state: dict = {}) -> Dict[str, Union[int, str, list]]:
        """
        Helper function to pop values from the state if we need to break out of pagination.

        :return: state
        """
        for key in (
            LAST_SEARCH_FROM,
            LAST_SEARCH_TO,
            CURRENT_COUNT,
            QUERY_START_TIME,
            QUERY_END_TIME,
        ):
            state.pop(key, None)

        return state

    def get_alert_limit(self, custom_config: dict) -> int:
        """
        Set the alert limit from CPS if it exists, otherwise default to ALERT_LIMIT
        Safety check if user tries to make search greater than 100

        :param custom_config: Custom config dict to parse for alert limit

        :return: Alert limit integer
        """

        alert_limit = custom_config.get("alert_limit", ALERT_LIMIT)

        if alert_limit > ALERT_LIMIT:
            self.logger.info(f"Alert limit exceeds {ALERT_LIMIT}, falling back to {ALERT_LIMIT}")
            alert_limit = ALERT_LIMIT

        return alert_limit
