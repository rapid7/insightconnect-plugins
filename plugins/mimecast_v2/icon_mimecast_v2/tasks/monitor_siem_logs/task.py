import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import APIException, PluginException
from insightconnect_plugin_runtime.helper import hash_sha1
from insightconnect_plugin_runtime.telemetry import monitor_task_delay
from .schema import (
    MonitorSiemLogsInput,
    MonitorSiemLogsOutput,
    MonitorSiemLogsState,
    Component,
)
from typing import Any, Dict, List, Tuple, Union
from logging import getLevelName
from datetime import datetime, timezone, timedelta, date
import copy

# Date format for conversion
DATE_FORMAT = "%Y-%m-%d"

# SIEM log types
RECEIPT = "receipt"
URL_PROTECT = "url protect"
ATTACHMENT_PROTECT = "attachment protect"
LOG_TYPES = [RECEIPT, URL_PROTECT, ATTACHMENT_PROTECT]

# TTP log types
TTP_IMPERSONATION = "ttp_impersonation"
TTP_ATTACHMENT = "ttp_attachment"
TTP_URL = "ttp_url"
TTP_LOG_TYPES = [TTP_IMPERSONATION, TTP_ATTACHMENT, TTP_URL]

# Default and max values
DEFAULT_THREAD_COUNT = 10
DEFAULT_PAGE_SIZE = 100
MAX_LOOKBACK_DAYS = 7
HEADROOM_DAYS = 1
INITIAL_MAX_LOOKBACK_DAYS = 1
LARGE_LOG_SIZE_LIMIT = 6700  # This is 7000 - 300 to account for TTP logs (page size 100, max 3 types)
SMALL_LOG_SIZE_LIMIT = 250
LARGE_LOG_HASH_SIZE_LIMIT = 4800
SMALL_LOG_HASH_SIZE_LIMIT = 100

# Run type
INITIAL_RUN = "initial_run"
SUBSEQUENT_RUN = "subsequent_run"
PAGINATION_RUN = "pagination_run"

# Access keys for state and custom config
LOG_HASHES = "log_hashes"
LAST_LOG_HASH = "last_log_hash"
QUERY_CONFIG = "query_config"
QUERY_DATE = "query_date"
CAUGHT_UP = "caught_up"
NEXT_PAGE = "next_page"
SAVED_FILE_URL = "saved_file_url"
SAVED_FILE_POSITION = "saved_file_position"
FURTHEST_QUERY_DATE = "furthest_query_date"

# Access keys for custom config
THREAD_COUNT = "thread_count"
PAGE_SIZE = "page_size"
LOG_LIMITS = "log_limits"


class MonitorSiemLogs(insightconnect_plugin_runtime.Task):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_siem_logs",
            description=Component.DESCRIPTION,
            input=MonitorSiemLogsInput(),
            output=MonitorSiemLogsOutput(),
            state=MonitorSiemLogsState(),
        )

    @monitor_task_delay(timestamp_keys=[FURTHEST_QUERY_DATE], default_delay_threshold="7d")
    def run(self, params={}, state={}, custom_config={}):  # pylint: disable=unused-argument
        # Set log level
        log_level = self.get_log_level(custom_config.get("log_level", "info"))
        self.connection.api.set_log_level(log_level)

        # Save existing state in case of error
        existing_state = copy.deepcopy(state)
        try:
            # Calculate now datetime
            now_datetime = datetime.now(tz=timezone.utc)
            self.logger.info(f"TASK: Current time (UTC): {now_datetime.isoformat()}")

            # Get available TTP log types based on permissions
            available_ttp_log_types = self._get_available_ttp_log_types()

            # Detect run condition and log it
            run_condition = self.detect_run_condition(
                state.get(QUERY_CONFIG, {}), now_datetime.date(), available_ttp_log_types
            )
            self.logger.info(f"TASK: Run state is {run_condition}")

            # Update state, apply custom config, get furthest lookback date and max run lookback date
            state = self.update_state(state)
            page_size, thead_count, log_limit = self.apply_custom_config(state, run_condition, custom_config)
            furthest_lookback_date = self.get_furthest_lookback_date(state.get(QUERY_CONFIG, {}))
            max_run_lookback_date = self.get_max_lookback_date(
                now_datetime.date(), run_condition, bool(custom_config), furthest_lookback_date
            )

            # Prepare query parameters
            query_config = self.prepare_query_params(
                state.get(QUERY_CONFIG, {}), max_run_lookback_date, now_datetime.date()
            )

            # Get all SIEM logs
            siem_logs = self.get_all_siem_logs(run_condition, query_config, page_size, thead_count, log_limit)

            # Get all TTP logs only if we have not reached the total log limit
            ttp_logs = self.get_all_ttp_logs(query_config, now_datetime, available_ttp_log_types, page_size)

            # Log total number of logs retrieved
            if all_logs := siem_logs + ttp_logs:
                self.logger.info(
                    f"TASK: Total logs retrieved across all types (SIEM = {len(siem_logs)}, TTP = {len(ttp_logs)}): {len(all_logs)}"
                )
            else:
                self.logger.info("TASK: No new logs retrieved across all types (SIEM, TTP)")

            # Prepare exit state and determine if more pages exist
            exit_state, has_more_pages = self.prepare_exit_state(
                state, query_config, now_datetime.date(), furthest_lookback_date
            )

            # Return results
            return all_logs, exit_state, has_more_pages, 200, None
        except APIException as error:
            self.logger.error(
                f"Error: An API exception has occurred. Status code: {error.status_code} returned. Cause: {error.cause}. Error data: {error.data}.",
                exc_info=True,
            )
            return [], existing_state, False, error.status_code, error
        except PluginException as error:
            self.logger.error(
                f"Error: A Plugin exception has occurred. Cause: {error.cause}  Error data: {error.data}."
            )
            return [], existing_state, False, 500, error
        except Exception as error:
            self.logger.error(
                f"Error: Unknown exception has occurred. No results returned. Error Data: {error}", exc_info=True
            )
            return (
                [],
                existing_state,
                False,
                500,
                PluginException(preset=PluginException.Preset.UNKNOWN, data=error),
            )

    @staticmethod
    def detect_run_condition(query_config: Dict[str, Any], now_date: date, available_ttp_log_types: List[str]) -> str:
        """
        Return runtype based on query configuration

        :param query_config: Dictionary containing query configuration for each log type
        :type query_config: Dict

        :param now_date: The current date for determining run condition
        :type now_date: date

        :param available_ttp_log_types: List of TTP log types that the connection has permission to access.
        :type available_ttp_log_types: List[str]

        :return: runtype string
        :rtype: str
        """

        # If no query configuration exists, it's an initial run
        if not query_config:
            return INITIAL_RUN

        # If any log type is not caught up or has not queried for today, it's a pagination run
        for log_type, log_type_config in query_config.items():
            # Skip TTP logs that are no longer available due to no permissions set.
            if log_type in TTP_LOG_TYPES and log_type not in available_ttp_log_types:
                continue
            if not log_type_config.get(CAUGHT_UP) or str(now_date) not in log_type_config.get(QUERY_DATE):
                return PAGINATION_RUN

        # Otherwise, it's a subsequent run
        return SUBSEQUENT_RUN

    def get_furthest_lookback_date(self, query_config: Dict[str, Any]) -> date:
        """
        Get the furthest lookback date from the query configuration

        :param query_config: Dictionary containing query configuration for each log type
        :type query_config: Dict

        :return: furthest lookback date
        :rtype: datetime
        """

        # Initialize `furthest_date` as None
        furthest_date = None

        # For each log type in query config, convert query date to date object and compare to find the furthest date
        for log_type, log_type_config in query_config.items():
            # If `query_date` string does not exist in config, skip it
            if not (query_date_str := log_type_config.get(QUERY_DATE)):
                continue

            # If `query_date_str` cannot be converted to date object, skip it
            if log_date := self._deserialize_query_date_from_state(log_type, query_date_str):
                # As dates are being compared we need to convert datetime to date for TTP logs
                if isinstance(log_date, datetime):
                    log_date = log_date.date()

                # If `furthest_date` is None or `log_date` is before `furthest_date`, update `furthest_date` to `log_date`
                if furthest_date is None or log_date < furthest_date:
                    furthest_date = log_date

        return furthest_date

    def update_state(self, state: Dict[str, Any]) -> Dict:
        """
        Initialise state, validate state, apply custom config

        :param state: The current state dictionary containing query configuration
        :type state: Dict

        :return: Updated state dictionary with initialised log type configurations
        :rtype: Dict
        """

        all_log_types = LOG_TYPES + TTP_LOG_TYPES
        initial_log_type_config = {CAUGHT_UP: False}
        if not state:
            self.logger.info("TASK: Initializing first state...")
            state = {QUERY_CONFIG: {log_type: copy.deepcopy(initial_log_type_config) for log_type in all_log_types}}
        else:
            for log_type in all_log_types:
                if log_type not in state.get(QUERY_CONFIG, {}).keys():
                    self.logger.info(f"TASK: `{log_type}` missing from state. Initializing...")
                    state[QUERY_CONFIG][log_type] = copy.deepcopy(initial_log_type_config)
        return state

    def get_max_lookback_date(
        self,
        now_date: date,
        run_condition: str,
        custom_config: bool,
        last_query_date: datetime,
    ) -> datetime:
        """
        Get max lookback date for run condition

        :param now_date: The current date for calculating lookback
        :type now_date: date

        :param run_condition: Type of run being executed (initial, subsequent, or pagination)
        :type run_condition: str

        :param custom_config: Whether custom configuration is provided
        :type custom_config: bool

        :param last_query_date: The last date that was queried
        :type last_query_date: datetime

        :return: Maximum lookback date for the current run
        :rtype: datetime
        """

        max_run_lookback_days = MAX_LOOKBACK_DAYS
        if run_condition == INITIAL_RUN and not custom_config:
            max_run_lookback_days = INITIAL_MAX_LOOKBACK_DAYS
        max_run_lookback_date = now_date - timedelta(days=max_run_lookback_days)
        if last_query_date:
            if run_condition == PAGINATION_RUN and last_query_date == now_date - timedelta(
                days=(max_run_lookback_days + HEADROOM_DAYS)
            ):
                self.logger.info("TASK: Pagination run detected, allow completion of cutoff day logs retrieval.")
                max_run_lookback_date -= timedelta(days=HEADROOM_DAYS)
        return max_run_lookback_date

    def apply_custom_config(
        self, state: Dict, run_type: str, custom_config: Dict[str, Any] = {}
    ) -> Tuple[int, int, Dict[Any, Any]]:
        """
        Apply custom configuration for lookback, query date applies to start and end time of query.

        :param state: Current state dictionary.
        :type state: dict

        :param run_type: Type of run being executed.
        :type run_type: str

        :param custom_config: Custom configuration dictionary.
        :type custom_config: dict

        :return: Page size, thread count and log limit.
        :rtype: Tuple[int, int, dict]
        """

        # Parse custom config if provided
        custom_query_config = {}
        if custom_config:
            self.logger.info("TASK: Custom config detected")
            custom_query_config = custom_config.get("query_config", {})

        # If initial run, apply custom query dates to state
        if run_type == INITIAL_RUN:
            current_query_config = state.get(QUERY_CONFIG, {})
            for log_type, log_query_config in custom_query_config.items():
                log_query_date = log_query_config.get(QUERY_DATE, None)
                self.logger.info(f"TASK: Supplied lookback date of {log_query_date} for log type {log_type}")
                current_query_config[log_type] = {QUERY_DATE: log_query_date}

        page_size = max(1, min(custom_config.get(PAGE_SIZE, DEFAULT_PAGE_SIZE), DEFAULT_PAGE_SIZE))
        thread_count = max(1, custom_config.get(THREAD_COUNT, DEFAULT_THREAD_COUNT))
        log_limit = custom_config.get(LOG_LIMITS, {})
        return page_size, thread_count, log_limit

    def prepare_query_params(self, query_config: Dict, max_lookback_date: datetime, now_date: date) -> Dict:
        """
        Prepare query for request. Validate query dates, move forward when caught up

        :param query_config: Dictionary containing query configuration for each log type
        :type query_config: Dict

        :param max_lookback_date: The earliest date allowed for querying logs
        :type max_lookback_date: datetime

        :param now_date: The current date for validation and query preparation
        :type now_date: datetime

        :return: Updated query configuration dictionary with validated dates
        :rtype: Dict
        """

        for log_type, log_type_config in query_config.items():
            # Initialize current query date as now date, and query_date_str from query config state for log type
            query_date, query_date_str = now_date, log_type_config.get(QUERY_DATE)

            # If `query_date_str` exists, deserialize it based on log type (SIEM logs use date format, TTP logs use ISO format with time)
            if query_date_str:
                query_date = self._deserialize_query_date_from_state(log_type, query_date_str)
                log_type_config[QUERY_DATE] = query_date

            # If `query_date_str` does not exist or couldn't be deserialized, initialize it to `max_lookback_date`
            if not query_date_str:
                self.logger.info(
                    f"TASK: Query date for `{log_type}` log type is not present. Initializing a `{max_lookback_date}`"
                )
                log_type_config[QUERY_DATE] = (
                    max_lookback_date
                    if log_type not in TTP_LOG_TYPES
                    else datetime.combine(max_lookback_date, datetime.min.time()).replace(tzinfo=timezone.utc)
                )

            # ====== SIEM LOGS ======
            # If `query_date` is before `now_date` and log type not caught up, move `query_date` forward by one day
            elif log_type in LOG_TYPES and query_date < now_date and log_type_config.get(CAUGHT_UP) is True:
                self.logger.info(f"TASK (SIEM): Log type {log_type} has caught up for {query_date}")
                log_type_config[QUERY_DATE] = query_date + timedelta(days=1)
                log_type_config[CAUGHT_UP] = False
                log_type_config.pop(NEXT_PAGE, None)

            # ====== ALL LOG TYPES ======
            # Validate query date is within scope of max lookback date and now date
            # Also, update query date config to be date or datetime depending on log type for future comparisons and querying
            query_config[log_type] = self.validate_config_lookback(
                log_type, log_type_config, max_lookback_date, now_date
            )
        return query_config

    def validate_config_lookback(
        self, log_type: str, log_type_config: Dict, max_lookback_date: datetime, now_date: date
    ) -> Dict:
        """
        Ensures provided query date in scope of request time window

        :param log_type: The type of log being processed (e.g., receipt, url protect, attachment protect)
        :type log_type: str

        :param log_type_config: Configuration dictionary for a specific log type containing query parameters
        :type log_type_config: Dict

        :param max_lookback_date: The earliest date allowed for querying logs
        :type max_lookback_date: datetime

        :param now_date: The current date for validation bounds
        :type now_date: datetime

        :return: Updated log type configuration with validated query date
        :rtype: Dict
        """

        # Get query date from log type config
        query_date = log_type_config.get(QUERY_DATE)

        # If we have TTP logs (datetime), convert to date for comparison for lookback validation
        # But keep original query date in log type config for TTP logs fetching
        if isinstance(query_date, datetime):
            query_date = query_date.date()

        # Validate query date is within scope of max lookback date and now date
        if query_date < max_lookback_date:
            return {QUERY_DATE: self._format_date_for_log_type(log_type, max_lookback_date)}

        # If query date is after now date, set to now date
        if query_date > now_date:
            log_type_config[QUERY_DATE] = self._format_date_for_log_type(log_type, now_date)

        # Update query date in log type config
        return log_type_config

    @staticmethod
    def _format_date_for_log_type(log_type: str, target_date: date) -> Union[date, datetime]:
        """
        Format date for log type. Depending on log type, we need to return either a date or datetime object
        SIEM logs are queried by date, and TTP logs are queried by datetime.

        :param log_type:
        :type log_type: str

        :param target_date:
        :type target_date: date

        :return: Formatted date for log type
        :rtype: Union[date, datetime]
        """

        if log_type in TTP_LOG_TYPES:
            return datetime.combine(target_date, datetime.min.time()).replace(tzinfo=timezone.utc)
        return target_date

    def get_all_siem_logs(
        self,
        run_condition: str,
        query_config: Dict,
        page_size: int,
        thead_count: int,
        log_limits: Dict = {},
    ) -> List[Any]:
        """
        Gets all logs of provided log type. First retrieves batch URLs. Then downloads and reads batches, pooling logs.

        :param run_condition: Type of run being executed (initial, subsequent, or pagination)
        :type run_condition: str

        :param query_config: Configuration dictionary containing query parameters for each log type
        :type query_config: Dict

        :param page_size: Number of records to retrieve per page
        :type page_size: int

        :param thead_count: Number of threads to use for parallel processing
        :type thead_count: int

        :param log_limits: Optional limits for log retrieval per log type
        :type log_limits: Dict

        :return: Logs, updated query configuration (state)
        :rtype: Tuple[List, Dict]
        """

        # Init list to hold all logs, and iterate through each log type to fetch logs
        complete_logs = []
        for log_type, log_type_config in query_config.items():
            if log_type in LOG_TYPES:
                if (not log_type_config.get(CAUGHT_UP)) or (run_condition != PAGINATION_RUN):
                    # Receipt logs are much higher volume than others, so should make up the bulk of the logs queried
                    log_size_limit = LARGE_LOG_SIZE_LIMIT if log_type == RECEIPT else SMALL_LOG_SIZE_LIMIT
                    if log_limits:
                        log_size_limit = log_limits.get(log_type, log_size_limit)
                    logs, results_next_page, caught_up, saved_file, saved_position = self.connection.api.get_siem_logs(
                        log_type=log_type,
                        query_date=log_type_config.get(QUERY_DATE),
                        next_page=log_type_config.get(NEXT_PAGE),
                        page_size=page_size,
                        max_threads=thead_count,
                        starting_url=log_type_config.get(SAVED_FILE_URL),
                        starting_position=log_type_config.get(SAVED_FILE_POSITION, 0),
                        log_size_limit=log_size_limit,
                    )
                    log_hash_size_limit = (
                        LARGE_LOG_HASH_SIZE_LIMIT if log_type == RECEIPT else SMALL_LOG_HASH_SIZE_LIMIT
                    )
                    deduplicated_logs, log_hashes = self.compare_and_dedupe_hashes(
                        log_type_config.get(LOG_HASHES, []), logs, log_hash_size_limit
                    )
                    self.logger.info(
                        f"TASK: (SIEM) Number of logs after de-duplication: {len(deduplicated_logs)} for log type {log_type}"
                    )
                    complete_logs.extend(deduplicated_logs)
                    log_type_config.update(
                        {
                            NEXT_PAGE: results_next_page,
                            CAUGHT_UP: caught_up,
                            LOG_HASHES: log_hashes,
                            SAVED_FILE_URL: saved_file,
                            SAVED_FILE_POSITION: saved_position,
                        }
                    )
                else:
                    self.logger.info(
                        f"TASK: (SIEM) Query for {log_type} is caught up. Skipping as we are currently paginating"
                    )
        return complete_logs

    def get_all_ttp_logs(
        self,
        query_config: Dict[str, Any],
        now_datetime: datetime,
        available_ttp_log_types: List[str],
        page_size: int = DEFAULT_PAGE_SIZE,
    ) -> List[Dict[str, Any]]:
        """
        Retrieve all available TTP logs for permitted log types within the specified time window.

        :param query_config: Query configuration for each log type.
        :type query_config: dict

        :param now_datetime: The current datetime used as the upper bound for log retrieval.
        :type now_datetime: datetime

        :param available_ttp_log_types: List of TTP log types that the connection has permission to access.
        :type available_ttp_log_types: List[str]

        :param page_size: Number of records to retrieve per page.
        :type page_size: int

        :return: List of retrieved TTP logs.
        :rtype: list of dict
        """

        # Initialize list to hold all completed logs
        completed_logs = []
        for log_type in available_ttp_log_types:
            # Retrieve query parameters (Moving time window approach)
            query_date_from = query_config.get(log_type, {}).get(QUERY_DATE)
            query_date_to = (
                (now_datetime - timedelta(seconds=1)).replace(microsecond=0).isoformat()
            )  # Now - 1 second to make sure we don't miss any logs
            pagination_token = query_config.get(log_type, {}).get(NEXT_PAGE)
            self.logger.info(
                f"TASK: ({log_type.upper()}) Retrieving TTP logs for log type `{log_type}` from date `{query_date_from}`"
            )

            # If `query_date` is datetime object, convert to ISO format string
            if isinstance(query_date_from, datetime):
                query_date_from = query_date_from.replace(microsecond=0).isoformat()

            # Fetch logs using the connection's API, and extend to completed_logs
            logs, next_page_token = self.connection.api.get_ttp_log(
                log_type, query_date_from, query_date_to, pagination_token, page_size=page_size
            )

            # Extend logs if any are returned
            if logs:
                self.logger.info(
                    f"TASK: ({log_type.upper()}) Found total of {len(logs)} logs for log type `{log_type}`. Extending to all received TTP logs."
                )
                completed_logs += logs
            else:
                self.logger.info(f"TASK: ({log_type.upper()}) No new logs found for log type `{log_type}`.")

            # Check if next_page_token is None to determine pagination
            if next_page_token:
                self.logger.info(
                    f"TASK: ({log_type.upper()}) The next page token for `{log_type}` is present. Saving it in state for next run."
                )
                query_config[log_type][NEXT_PAGE] = next_page_token
                query_config[log_type][CAUGHT_UP] = False
            else:
                # No next page token, so remove it from state and update query date to now
                self.logger.info(
                    f"TASK: ({log_type.upper()}) No next page token for `{log_type}`. Removing `next_page` from state."
                )
                query_config[log_type].pop(NEXT_PAGE, None)
                query_config[log_type][CAUGHT_UP] = True
                query_config[log_type][QUERY_DATE] = now_datetime.replace(
                    microsecond=0
                ).isoformat()  # This is bumped by 1 seconds from `query_date_to` to set boundary for next run

        self.logger.info(f"TASK: (TTP) Total TTP logs retrieved across all types: {len(completed_logs)}")
        return completed_logs

    def _get_available_ttp_log_types(self) -> List[str]:
        """
        Get available TTP log types based on permissions. Filter out TTP log types if no permission.

        :return:
        :rtype: List[str]
        """

        return [log_type for log_type in self.connection.api.validate_permissions("TTP") if log_type in TTP_LOG_TYPES]

    @staticmethod
    def compare_and_dedupe_hashes(
        previous_logs_hashes: list,
        new_logs: list,
        log_hash_size_limit: int = SMALL_LOG_HASH_SIZE_LIMIT,
    ) -> Tuple[list, list]:
        """
        Iterate through two lists of values, hashing each. Compare hash value to a list of existing hash values.
        If the hash exists, return both it and the value in separate lists once iterated.

        :param previous_logs_hashes: List of existing hashes to compare against.
        :type previous_logs_hashes: list

        :param new_logs: New values to hash and compare to existing list of hashes.
        :type new_logs: list

        :param log_hash_size_limit: Limit of hashes to return in order to reduce state size. Defaults to SMALL_LOG_HASH_SIZE_LIMIT.
        :type log_hash_size_limit: int

        :return: Hex digest of hash.
        :rtype: Tuple[list, list]
        """

        new_logs_hashes = []
        logs_to_return = []
        # Limit the amount of log hashes saved in order to reduce state size
        log_hash_save_start = len(new_logs) - log_hash_size_limit
        new_logs.sort(key=lambda x: x["timestamp"])
        for index, log in enumerate(new_logs):
            hash_ = hash_sha1(log)
            if hash_ not in previous_logs_hashes:
                logs_to_return.append(log)
                if index >= log_hash_save_start:
                    new_logs_hashes.append(hash_)
        return logs_to_return, new_logs_hashes

    def prepare_exit_state(
        self, state: dict, query_config: dict, now_date: datetime, furthest_query_date: datetime
    ) -> Tuple[Dict, bool]:
        """
        Prepare state and pagination for task completion. Format date time.

        :param state: The current state dictionary containing task configuration
        :type state: dict

        :param query_config: Dictionary containing query configuration for each log type
        :type query_config: dict

        :param now_date: The current date for comparison and pagination logic
        :type now_date: datetime

        :param furthest_query_date: The earliest date from all log type configurations
        :type furthest_query_date: datetime

        :return: Updated state dictionary and boolean indicating if more pages exist
        :rtype: Tuple[Dict, bool]
        """

        # Determine if pagination is required
        has_more_pages = False
        for log_type, log_type_config in query_config.items():
            # For SIEM logs
            if log_type in LOG_TYPES:
                query_date = log_type_config.get(QUERY_DATE)
                if isinstance(query_date, str):
                    query_date = datetime.strptime(query_date, DATE_FORMAT).date()

                # If log type not caught up or query date is before now date set `has_more_pages` to True
                if (not log_type_config.get(CAUGHT_UP)) or self._is_query_date_behind(query_date, now_date):
                    has_more_pages = True

                # Format query date to string for store in state
                log_type_config[QUERY_DATE] = query_date.strftime(DATE_FORMAT)

            # For TTP logs
            if log_type in TTP_LOG_TYPES:
                if NEXT_PAGE in log_type_config:
                    has_more_pages = True

        # If furthest query date exists format it to string, otherwise set to None
        if furthest_query_date:
            furthest_query_date_str = furthest_query_date.strftime("%Y-%m-%d")
        else:
            furthest_query_date_str = None

        # Serialize query dates for state storage
        query_config = self._serialize_query_dates_for_state(query_config)

        # Update state fields for next run and return
        state[QUERY_CONFIG] = query_config
        state[FURTHEST_QUERY_DATE] = furthest_query_date_str
        return state, has_more_pages

    @staticmethod
    def _serialize_query_dates_for_state(query_config: Dict[str, Any]) -> Dict[str, str]:
        """
        Serialize query dates in query config to string format for state storage.
        Convert date or datetime objects to string format depending on log type.

        :param query_config:
        :type query_config: Dict[str, Any]

        :return: Updated query config with serialized query dates for state storage
        :rtype: Dict[str, str]
        """

        # Iterate through query config and convert any datetime or date objects to string format for state storage
        for log_type, log_type_config in query_config.items():
            # Get query date and convert to string format depending on type
            query_date = log_type_config.get(QUERY_DATE)

            # TTP logs use ISO format with time, so convert datetime to ISO format string
            # Check datetime first since datetime is a subclass of date
            if log_type in TTP_LOG_TYPES and isinstance(query_date, datetime):
                log_type_config[QUERY_DATE] = query_date.replace(microsecond=0).isoformat()

            # SIEM logs use date format
            elif log_type in LOG_TYPES and isinstance(query_date, date):
                log_type_config[QUERY_DATE] = query_date.strftime(DATE_FORMAT)
        return query_config

    def _deserialize_query_date_from_state(self, log_type: str, query_date_string: str) -> Union[datetime, date]:
        """
        Deserialize query date from state string format to date or datetime object depending on log type. If deserialization fails, return None.

        :param log_type:
        :type log_type: str

        :param query_date_string:
        :type query_date_string: str

        :return:
        :rtype: Union[datetime, date]
        """

        # Deserialize based on log type
        try:
            # SIEM logs use (YYYY-MM-DD), so convert to date object
            if log_type in LOG_TYPES:
                return datetime.strptime(query_date_string, DATE_FORMAT).date()
            # TTP logs use ISO format with time, so convert to datetime object
            elif log_type in TTP_LOG_TYPES:
                return datetime.fromisoformat(query_date_string).replace(tzinfo=timezone.utc)
        except (ValueError, TypeError) as error:
            self.logger.error(
                f"TASK: Error deserializing query date `{query_date_string}` for log type `{log_type}`. Error: {error}",
                exc_info=True,
            )
            raise error

    @staticmethod
    def _is_query_date_behind(query_date: Union[datetime, date], now_date: date) -> bool:
        """
        Check if query date is behind the current date, handling both datetime and date objects.

        :param query_date: The query date to compare (datetime or date object)
        :param now_date: The current date for comparison

        :return: True if query date is behind current date
        """

        if isinstance(query_date, datetime):
            return query_date.date() < now_date
        return query_date < now_date

    @staticmethod
    def get_log_level(log_level: str = "info") -> int:
        log_level_mappings = {
            "INFO": "DEBUG",  # we want to keep logging to a minimal so don't print our debug logs
            "DEBUG": "INFO",
            # we want to change loggers in this task to be of type "info" and included for traceability
        }
        return getLevelName(log_level_mappings.get(log_level.upper()))
