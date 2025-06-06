import insightconnect_plugin_runtime
from requests import Response

from .schema import (
    MonitorAlertsInput,
    MonitorAlertsOutput,
    MonitorAlertsState,
    Component,
)
from datetime import datetime, timedelta, timezone
from insightconnect_plugin_runtime.exceptions import PluginException, APIException
from insightconnect_plugin_runtime.helper import hash_sha1
from typing import Tuple, List, Dict, Any
from dataclasses import dataclass


TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
MAX_LOOKBACK_DAYS = 7
DEFAULT_LOOKBACK_HOURS = 24
HEADROOM_MINUTES = 60
# This is the max amount of alerts that can be returned by the API in search from -> search_to
ALERT_LIMIT = 100

# State held values
LAST_ALERT_HASH = "last_alert_hash"
CURRENT_COUNT = "current_count"
QUERY_START_TIME = "query_start_time"
QUERY_END_TIME = "query_end_time"
QUERY_SEARCH_FROM = "search_from"
QUERY_SEARCH_TO = "search_to"

# General Pagination
LAST_SEARCH_FROM = "last_search_from"
LAST_SEARCH_TO = "last_search_to"
ALERT_TIMESTAMP_KEY = "detection_timestamp"
ALERT_ID_KEY = "alert_id"
QUERY_TIMESTAMP_KEY = "creation_time"


@dataclass
class QueryValues:
    QUERY_START_TIME: int
    QUERY_END_TIME: int
    QUERY_SEARCH_FROM: int
    QUERY_SEARCH_TO: int


class MonitorAlerts(insightconnect_plugin_runtime.Task):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_alerts",
            description=Component.DESCRIPTION,
            input=MonitorAlertsInput(),
            output=MonitorAlertsOutput(),
            state=MonitorAlertsState(),
        )

    def run(self, params={}, state={}, custom_config: dict = {}):  # pylint: disable=unused-argument
        existing_state = state.copy()

        try:
            alert_limit = self.get_alert_limit(custom_config=custom_config)
            now_time = datetime.utcnow()
            query_values = self.calculate_query_values(custom_config, now_time, existing_state, alert_limit)

            self.logger.info("Starting to download alerts...")

            response, state, has_more_pages = self.get_alerts_palo_alto(
                state=state, query_values=query_values, alert_limit=alert_limit
            )

            return response, state, has_more_pages, 200, None

        except APIException as error:
            return ([], existing_state, False, error.status_code, error)

        except PluginException as error:
            status_code = 500
            if isinstance(error.data, Response):
                # if there is response data in the error then use it in the exception
                if error.data.status_code != 200:
                    status_code = error.data.status_code
            self.logger.error(
                f"A PluginException has occurred. Status code {status_code} returned. Error: {error}. "
                f"Existing state: {existing_state}"
            )
            return [], existing_state, False, status_code, error

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
    def get_alerts_palo_alto(
        self, state: dict, query_values: QueryValues, alert_limit: int
    ) -> Tuple[List[Dict[str, Any]], Dict, bool]:

        post_body = self.build_post_body(
            search_from=query_values.QUERY_SEARCH_FROM,
            search_to=query_values.QUERY_SEARCH_TO,
            start_time=query_values.QUERY_START_TIME,
            end_time=query_values.QUERY_END_TIME,
        )

        results, _, total_count = self.connection.xdr_api.get_response_alerts(post_body)

        new_alerts, new_alert_hashes = self._dedupe_and_get_highest_time(results, state)

        state[CURRENT_COUNT] = state.get(CURRENT_COUNT, 0) + len(new_alerts)
        # We paginate if the total actual results returned in a page is equal to the alert limit
        is_paginating = len(results) >= alert_limit

        log_string = (
            f"search_from = {query_values.QUERY_SEARCH_FROM} "
            f"search_to = {query_values.QUERY_SEARCH_TO} "
            f"current_count = {state.get(CURRENT_COUNT, 0)} "
            f"total_count = {total_count}"
        )

        if is_paginating:
            state[QUERY_START_TIME] = query_values.QUERY_START_TIME
            state[QUERY_END_TIME] = query_values.QUERY_END_TIME
            state[LAST_SEARCH_FROM] = query_values.QUERY_SEARCH_FROM
            state[LAST_SEARCH_TO] = query_values.QUERY_SEARCH_TO
            self.logger.info(f"More pages available, saving existing search window to state: {log_string}")
        else:
            self.logger.info(f"Read all pages of alerts: {log_string}")
            state = {QUERY_END_TIME: query_values.QUERY_END_TIME}

        # update hashes in state only if we've got new ones
        state[LAST_ALERT_HASH] = new_alert_hashes if new_alert_hashes else state.get(LAST_ALERT_HASH, [])

        return new_alerts, state, is_paginating

    ###########################
    # Deduping
    ###########################
    def _dedupe_and_get_highest_time(self, alerts: list, state: dict) -> Tuple[list, list, int]:
        """
        Function to dedupe alerts using existing hashes in the state, and return the highest
        timestamp.

        :param alerts: list of alerts
        :param state: state of the plugin

        :return: list of unique alerts, list of new hashes
        """
        old_hashes = state.get(LAST_ALERT_HASH, [])
        deduped_alerts = 0
        new_alerts = []
        new_hashes = []
        highest_timestamp = 0

        # Create a new hash for every new alert
        for alert in alerts:
            # Hash the current alert
            alert_hash = hash_sha1(alert)
            # Add this new hash to the new hash list
            new_hashes.append(alert_hash)
            # Check to see if this new hash is in the list of old hashes
            if alert_hash in old_hashes:
                # If it is, add it to the deduped alerts
                deduped_alerts += 1
            # Otherwise
            else:
                # Add this new unique alert to undeduped (the whole object, not the hash)
                new_alerts.append(alert)

        # If len is 0, all results are deduped so we get list index error, so do quick if check
        if len(new_alerts) > 0:
            # Get the timestamp of the latest alert in the list of results
            highest_timestamp = new_alerts[-1].get(ALERT_TIMESTAMP_KEY)

        self.logger.info(f"Received {len(alerts)} alerts")
        self.logger.info(f"Number of duplicates found: {deduped_alerts}")
        self.logger.info(f"Number of new alerts found: {len(new_alerts)}")
        self.logger.debug(f"Last alert timestamp is {highest_timestamp}")
        self.logger.debug(f"Last hash is {new_hashes}")

        return new_alerts, new_hashes

    def calculate_query_values(
        self,
        custom_config: dict,
        now_date_time: datetime,
        saved_state: dict,
        alert_limit: int,
    ) -> QueryValues:
        """
        Takes custom config from CPS and allows the specification of a new start time for alerts,
        and allows the limit to be customised.

        :param custom_config: custom_config for the plugin
        :param now_unix: datetime representing 'now' in unix
        :param saved_state: existing state of the integration
        :param: alert_limit: Maximum results per page
        :return: QueryValues: Get Alerts query input values
        """
        default_end_time = now_date_time - timedelta(minutes=15)
        start_time, end_time, max_lookback_date_time = self.get_query_times(
            saved_state, now_date_time, default_end_time
        )
        search_from = saved_state.get(LAST_SEARCH_TO, 0)
        search_to = saved_state.get(LAST_SEARCH_TO, 0) + alert_limit
        if custom_config:
            self.logger.info("Custom config detected")
            start_time, max_lookback_date_time = self._parse_custom_config(custom_config, now_date_time, start_time)

        # Non pagination run
        if not start_time:
            start_time = now_date_time - timedelta(hours=DEFAULT_LOOKBACK_HOURS)
            end_time = default_end_time

        # Check start_time in comparison to max_lookback
        if start_time.replace(tzinfo=timezone.utc) < max_lookback_date_time.replace(tzinfo=timezone.utc):
            self.logger.info(f"Start time of {start_time} exceeds cutoff of {max_lookback_date_time}")
            start_time = max_lookback_date_time + timedelta(minutes=HEADROOM_MINUTES)
            self.logger.info("Adjusting start time to appropriate cutoff value")
            self.logger.info("Resetting search_from and search_to")
            search_from = 0
            search_to = alert_limit
        self.logger.info(f"Setting query start time to {start_time}")
        self.logger.info(f"Setting query end time to {end_time}")
        return QueryValues(
            QUERY_START_TIME=self.convert_datetime_to_unix(start_time),
            QUERY_END_TIME=self.convert_datetime_to_unix(end_time),
            QUERY_SEARCH_FROM=search_from,
            QUERY_SEARCH_TO=search_to,
        )

    def get_query_times(self, state, now_date_time, default_end_time) -> Tuple[datetime, datetime, datetime]:
        """
        Get initial query times in unix for get alerts query, and max lookback date time
        :param state:
        :param now_date_time:
        :param default_end_time:
        :return: start time, end time, max lookback date time
        """
        last_query_start_time = state.get(QUERY_START_TIME)
        last_query_end_time = state.get(QUERY_END_TIME)
        max_lookback_date_time = now_date_time - timedelta(days=MAX_LOOKBACK_DAYS)

        last_query_start_time = self.convert_unix_to_datetime(last_query_start_time) if last_query_start_time else None
        last_query_end_time = self.convert_unix_to_datetime(last_query_end_time) if last_query_end_time else None
        if last_query_start_time and last_query_end_time:
            self.logger.info("More pages available, attempting to retain query start and end times")
            start_time = last_query_start_time
            end_time = last_query_end_time
        else:
            start_time = last_query_end_time
            end_time = default_end_time
        return start_time, end_time, max_lookback_date_time

    ###########################
    # Custom Config
    ###########################
    def _parse_custom_config(self, custom_config, now_datetime, start_time) -> Tuple[int, datetime]:
        """
        Retrieve values from custom config
        :param custom_config:
        :param now_datetime:
        :param start_time:
        :return: start time, maxlookback time
        """
        # Get custom config lookback value only if start_time in state is cleared
        custom_timings = custom_config.get("lookback", {})
        custom_date = custom_timings.get("date")
        custom_hours = custom_timings.get("hours", DEFAULT_LOOKBACK_HOURS)
        if not start_time:
            self.logger.info("Task is in its first run")
            start_time = datetime(**custom_date) if custom_date else (now_datetime - timedelta(hours=custom_hours))

        # Get max lookback from custom config
        max_lookback_days = custom_config.get("max_lookback_days", MAX_LOOKBACK_DAYS)
        max_lookback_date_time = custom_config.get("max_lookback_date_time", {})
        max_lookback = (
            datetime(**max_lookback_date_time)
            if max_lookback_date_time
            else now_datetime - timedelta(days=max_lookback_days)
        )

        return start_time, max_lookback

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
            {"field": QUERY_TIMESTAMP_KEY, "operator": "gte", "value": start_time},
            {"field": QUERY_TIMESTAMP_KEY, "operator": "lte", "value": end_time},
        ]

        post_body = {
            "request_data": {
                "search_from": search_from,
                "search_to": search_to,
                "sort": {"field": QUERY_TIMESTAMP_KEY, "keyword": "asc"},
                "filters": filters,
            }
        }

        self.logger.debug(f"Post Body: {post_body}")

        return post_body

    ###########################
    # Datetime Helpers
    ###########################
    def convert_unix_to_datetime(self, unix_time: int) -> datetime:
        # Convert a unix timestamp to a datetime object
        return datetime.fromtimestamp(unix_time / 1000, tz=timezone.utc)

    def convert_datetime_to_unix(self, date_time: datetime) -> int:
        # Ensure the datetime object is in UTC
        if date_time.tzinfo is None:
            date_time = date_time.replace(tzinfo=timezone.utc)
        return int(date_time.timestamp() * 1000)

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
