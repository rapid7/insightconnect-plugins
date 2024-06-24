import insightconnect_plugin_runtime
import requests
from insightconnect_plugin_runtime.exceptions import HTTPStatusCodes, PluginException
from insightconnect_plugin_runtime.helper import extract_json, response_handler
from .schema import (
    MonitorActivitiesAndEventsInput,
    MonitorActivitiesAndEventsOutput,
    MonitorActivitiesAndEventsState,
    Input,
    Output,
    Component,
    State,
)
from komand_sentinelone.util.exceptions import ApiException

# Custom imports below
from datetime import datetime, timezone, timedelta
from typing import List, Dict, Tuple, Optional

# State values
LAST_RUN_TIMESTAMP = "last_run_timestamp"
ACTIVITIES_LAST_LOG_TIMESTAMP = "activities_last_log_timestamp"
EVENTS_LAST_LOG_TIMESTAMP = "events_last_log_timestamp"
THREATS_LAST_LOG_TIMESTAMP = "threats_last_log_timestamp"
ACTIVITIES_PAGE_CURSOR = "activities_page_cursor"
EVENTS_PAGE_CURSOR = "events_page_cursor"
THREATS_PAGE_CURSOR = "threats_page_cursor"

# Cutoff values
DATE_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
INITIAL_CUTOFF_HOURS = 24
MAX_CUTOFF_HOURS = 24 * 7
LOGS_PAGE_LIMIT = 1000

API_VERSION = "2.1"
STARTING_TIMESTAMP = "1900-01-01T00:00:00.000000Z"

ACTIVITIES_LOGS = "activities_logs"
EVENTS_LOGS = "events_logs"
THREATS_LOGS = "threats_logs"

LOG_TYPE_MAP = {
    ACTIVITIES_LOGS: {"LAST_LOG_TIMESTAMP": ACTIVITIES_LAST_LOG_TIMESTAMP, "PAGE_TOKEN": ACTIVITIES_PAGE_CURSOR},
    EVENTS_LOGS: {"LAST_LOG_TIMESTAMP": EVENTS_LAST_LOG_TIMESTAMP, "PAGE_TOKEN": EVENTS_PAGE_CURSOR},
    THREATS_LOGS: {"LAST_LOG_TIMESTAMP": THREATS_LAST_LOG_TIMESTAMP, "PAGE_TOKEN": THREATS_PAGE_CURSOR},
}


class MonitorActivitiesAndEvents(insightconnect_plugin_runtime.Task):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_activities_and_events",
            description=Component.DESCRIPTION,
            input=MonitorActivitiesAndEventsInput(),
            output=MonitorActivitiesAndEventsOutput(),
            state=MonitorActivitiesAndEventsState(),
        )

    def run(self, params={}, state={}, custom_config={}):
        """
        Query activities, device control events, and threats logs between a supplied timeframe and the current time.
        Return all found logs and set last task run time, pagination cursors, and last log timestamps for each log type.
        """
        existing_state = state.copy()
        try:
            is_initial_run = self.check_initial_run(state)
            queries = self.check_queries(params)
            cursors = self.get_cursors(state)
            total_queries = self.count_queries(queries)
            total_forbidden_responses = 0
            last_run_timestamp = state.get(LAST_RUN_TIMESTAMP)
            self.logger.info(cursors)
            is_paginating = any(cursors.values())
            if is_paginating:
                self.log_pagination_cycle(cursors)

            current_run_timestamp, lookback_timestamp = self.get_lookback_values(
                is_initial_run, custom_config, last_run_timestamp
            )

            all_logs, total_forbidden_responses = self.collect_logs_handler(
                queries,
                cursors,
                state,
                lookback_timestamp,
                current_run_timestamp,
                total_forbidden_responses,
                is_paginating,
            )

            # Check if all ran queries have returned 401 or 403 errors and raise an exception if so
            if total_forbidden_responses >= total_queries > 0:
                return [], existing_state, False, 401, PluginException(preset=PluginException.Preset.UNAUTHORIZED)
            has_more_pages = self.determine_next_pagination_cycle(state, lookback_timestamp, current_run_timestamp)
            return all_logs, state, has_more_pages, 200, None
        except ApiException as error:
            return [], existing_state, False, error.status_code, error
        except Exception as error:
            return [], existing_state, False, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def check_initial_run(self, state: Dict) -> bool:
        """
        Check if state exists, return False if so indicating initial run
        """
        is_initial_run = not state
        if is_initial_run:
            self.logger.info("No state detected. Instantiating initial run.")
        else:
            self.logger.info("State detected. Instantiating continuation run.")
        return is_initial_run

    def check_queries(self, params: Dict) -> Tuple[str, str, str]:
        """
        Return whether to query a specific endpoint based on the input parameters
        """
        queries = {
            ACTIVITIES_LOGS: params.get(Input.COLLECTACTIVITIES),
            EVENTS_LOGS: params.get(Input.COLLECTEVENTS),
            THREATS_LOGS: params.get(Input.COLLECTTHREATS),
        }
        return queries

    def get_cursors(self, state: Dict) -> Tuple[str, str, str]:
        """
        Return existing cursors for each endpoint
        """
        cursors = {
            ACTIVITIES_LOGS: state.get(ACTIVITIES_PAGE_CURSOR),
            EVENTS_LOGS: state.get(EVENTS_PAGE_CURSOR),
            THREATS_LOGS: state.get(THREATS_PAGE_CURSOR),
        }
        return cursors

    def count_queries(self, queries: dict) -> int:
        "Count how many queries are to be made and return the value"
        total_queries = 0
        for query in queries.values():
            if query is not None:
                total_queries += 1
        return total_queries

    def log_pagination_cycle(self, cursors) -> None:
        """
        Provide logging information if task is in pagination cycle
        """
        pagination_info_string = "Pagination tokens received... "
        for log_type, cursor in cursors.items():
            if cursor is not None:
                pagination_info_string += f" {log_type}:{cursor}"
        self.logger.info("Paginating cycle in progress.")
        self.logger.info(pagination_info_string)

    def collect_logs_handler(
        self,
        queries: Dict,
        cursors: Dict,
        state: Dict,
        lookback_timestamp: str,
        current_run_timestamp: str,
        total_forbidden_responses: int,
        is_paginating: bool,
    ) -> Tuple[List[Dict], int]:
        """
        Handle whether to query each endpoint based on input and pagination, gather returned data and error responses
        """
        all_logs = []
        for log_type, check in queries.items():
            if check:
                cursor = cursors.get(log_type)
                if is_paginating is False or (is_paginating is True and cursor):
                    self.logger.info(f"Getting {log_type} between {lookback_timestamp} and {current_run_timestamp}...")
                    if cursor:
                        self.logger.info(f"Using next page cursor: {cursor}")
                    logs, total_forbidden_responses = self.get_generic_logs(
                        log_type,
                        state,
                        total_forbidden_responses,
                        current_run_timestamp,
                        lookback_timestamp,
                        cursor,
                    )
                    self.logger.info(f"{len(logs)} logs found in {log_type} query")
                    all_logs.extend(logs)
                else:
                    self.logger.info(f"Pagination in progress, skipping {log_type} collection...")
        return all_logs, total_forbidden_responses

    def get_generic_logs(
        self,
        log_type: str,
        state: dict,
        total_forbidden_responses: int,
        current_run_timestamp: str,
        last_run_timestamp: str = None,
        pagination_cursor: str = None,
    ) -> List[Dict]:
        """
        Determine log type and query that log set with query parameters determined by type, cursor, and last timestamp.
        Set latest log timestamp and page cursor in state.
        Return logs from query
        """
        timestamp_key = LOG_TYPE_MAP.get(log_type, {}).get("LAST_LOG_TIMESTAMP")
        page_token_key = LOG_TYPE_MAP.get(log_type, {}).get("PAGE_TOKEN")
        last_log_timestamp = state.get(timestamp_key)
        if not last_log_timestamp:
            last_log_timestamp = STARTING_TIMESTAMP
        query_params = self.get_query_params(log_type, last_run_timestamp, current_run_timestamp, pagination_cursor)
        if log_type == ACTIVITIES_LOGS:
            response = self.connection.client.get_activities_list(query_params, True, False)
        elif log_type == EVENTS_LOGS:
            response = self.connection.client.get_device_control_events(query_params, True, False)
        else:
            response = self.connection.client.get_threats(query_params, API_VERSION, True, False)
        try:
            status_code = response.status_code
            if response.status_code in [401, 403]:
                self.logger.info(f"Received status code {status_code} for {log_type} query")
            response_handler(response, allowed_status_codes=[401, 403])
        except PluginException as error:
            raise ApiException(cause=error.cause, assistance=error.assistance, status_code=status_code, data=response)
        logs, next_page_cursor, total_forbidden_responses = self.extract_query_response(
            response, total_forbidden_responses
        )
        new_logs_last_timestamp = self.get_latest_timestamp(logs, last_log_timestamp)
        state[timestamp_key] = new_logs_last_timestamp
        state[page_token_key] = next_page_cursor
        if next_page_cursor:
            self.logger.info(f"New next page cursor received for {log_type}: {next_page_cursor}")
        return logs, total_forbidden_responses

    def get_query_params(self, log_type: str, last_log_timestamp: str, current_run_timestamp: str, cursor: str) -> Dict:
        """
        Generate query parameters based on log type and availability of pagination cursor
        """
        timestamp_name = "createdAt"
        if log_type == EVENTS_LOGS:
            timestamp_name = "eventTime"
        query_params = {
            "limit": LOGS_PAGE_LIMIT,
            f"{timestamp_name}__gt": last_log_timestamp,
            f"{timestamp_name}__lte": current_run_timestamp,
            "sortBy": timestamp_name,
        }
        if cursor:
            query_params["cursor"] = cursor
        return query_params

    def extract_query_response(
        self, response: requests.Response, total_forbidden_responses: int
    ) -> Tuple[List[Dict], str]:
        """
        Return the log sand the pagination cursor from a query response
        """
        if response.status_code in [HTTPStatusCodes.UNAUTHORIZED, HTTPStatusCodes.FORBIDDEN]:
            total_forbidden_responses += 1
            return [], None, total_forbidden_responses
        response_json = extract_json(response)
        logs = response_json.get("data", [])
        next_cursor = response_json.get("pagination", {}).get("nextCursor")
        return logs, next_cursor, total_forbidden_responses

    def get_latest_timestamp(self, logs, latest_timestamp_string) -> Optional[str]:
        """
        Return the latest timestamp from a sorted list of logs. If no logs exist, use the last provided timestamp
        """
        # If no logs returned, return existing timestamp or None if never previously set
        if len(logs) == 0:
            if latest_timestamp_string == STARTING_TIMESTAMP:
                return None
            return latest_timestamp_string
        new_timestamp_string = logs[-1].get("createdAt")
        if new_timestamp_string is None:
            new_timestamp_string = logs[-1].get("threatInfo", {}).get("createdAt")
        new_timestamp = datetime.strptime(new_timestamp_string, DATE_TIME_FORMAT).astimezone(timezone.utc)
        latest_timestamp = datetime.strptime(latest_timestamp_string, DATE_TIME_FORMAT).astimezone(timezone.utc)
        if new_timestamp > latest_timestamp:
            latest_timestamp_string = new_timestamp_string
        return latest_timestamp_string

    def determine_next_pagination_cycle(self, state: dict, lookback_timestamp: str, current_run_timestamp: str) -> bool:
        """
        Set the last run timestamp in state based upon pagination cycle.
        Return true if pagination expected next cycle.
        """
        has_more_pages = any(
            [state.get(ACTIVITIES_PAGE_CURSOR), state.get(EVENTS_PAGE_CURSOR), state.get(THREATS_PAGE_CURSOR)]
        )
        if has_more_pages:
            self.logger.info(
                "Pagination token was returned. Not updating last run timestamp to current time until query completed."
            )
            state[LAST_RUN_TIMESTAMP] = lookback_timestamp
        else:
            state[LAST_RUN_TIMESTAMP] = current_run_timestamp
        return has_more_pages

    def get_lookback_values(
        self, is_initial_run: bool, custom_config: dict = {}, last_timestamp: str = None
    ) -> Tuple[str, str]:
        """
        Determine cutoff hours from running state, or supplied custom config cutoff hours which take precedent.
        Determine a lookback date from last run timestamp or, if not available, from the determined cutoff hours.
        If a custom lookback date is supplied in the custom config, use this as a lookback date for initial runs.
        Return the current date and the calculated lookback date time
        """
        # Get the current time
        current_date_time = datetime.now(timezone.utc)
        lookback_date = None
        if custom_config:
            self.logger.info("Custom config detected")
        # Set the lookback date to the last timestamp if it exists
        if last_timestamp:
            lookback_date = datetime.strptime(last_timestamp, DATE_TIME_FORMAT).astimezone(timezone.utc)
            self.logger.info(f"Last run timestamp found: {lookback_date}")
        # Determine cutoff date based on running state, default cutoff hours, and supplied custom config cutoff hours
        default_cutoff_hours = INITIAL_CUTOFF_HOURS if is_initial_run else MAX_CUTOFF_HOURS
        cutoff_hours = custom_config.get("cutoff_hours", default_cutoff_hours)
        cutoff_date = current_date_time - timedelta(hours=cutoff_hours)
        # limit the lookback to the cutoff. If there is no last timestamp, lookback to the cutoff
        if lookback_date is None or (lookback_date and lookback_date < cutoff_date):
            self.logger.info(f"Implementing cutoff hours: {cutoff_hours}")
            lookback_date = cutoff_date
        # Use a custom config lookback date if supplied and the task is in an initial run phase
        # Default and custom config cutoffs do not apply to this value
        custom_lookback_date = custom_config.get("lookback")
        if custom_lookback_date and is_initial_run:
            lookback_date = datetime(**custom_lookback_date, tzinfo=timezone.utc).astimezone()
            self.logger.info(f"Custom lookback date provided {lookback_date} and task is in first run")

        self.logger.info(f"Setting lookback date to {lookback_date}")
        lookback_date_string = datetime.strftime(lookback_date, DATE_TIME_FORMAT)
        current_date_time_string = datetime.strftime(current_date_time, DATE_TIME_FORMAT)
        return current_date_time_string, lookback_date_string
