import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import APIException, PluginException
from insightconnect_plugin_runtime.helper import hash_sha1
from insightconnect_plugin_runtime.telemetry import monitor_task_delay
from .schema import (
    MonitorSiemLogsInput,
    MonitorSiemLogsOutput,
    MonitorSiemLogsState,
    Input,
    Output,
    Component,
    State,
)
from typing import Dict, List, Tuple
from logging import getLevelName
from datetime import datetime, timezone, timedelta
import copy

# Date format for conversion
DATE_FORMAT = "%Y-%m-%d"
# Default and max values
RECEIPT = "receipt"
URL_PROTECT = "url protect"
ATTACHMENT_PROTECT = "attachment protect"
LOG_TYPES = [RECEIPT, URL_PROTECT, ATTACHMENT_PROTECT]
DEFAULT_THREAD_COUNT = 10
DEFAULT_PAGE_SIZE = 100
MAX_LOOKBACK_DAYS = 7
HEADROOM_DAYS = 1
INITIAL_MAX_LOOKBACK_DAYS = 1
LARGE_LOG_SIZE_LIMIT = 7000
SMALL_LOG_SIZE_LIMIT = 250
LARGE_LOG_HASH_SIZE_LIMIT = 4800
SMALL_LOG_HASH_SIZE_LIMIT = 100
# Run type
INITIAL_RUN = "initial_run"
SUBSEQUENT_RUN = "subsequent_run"
PAGINATION_RUN = "pagination_run"
# Access keys for state and custom config
LOG_HASHES = "log_hashes"
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

    @monitor_task_delay(timestamp_keys=[FURTHEST_QUERY_DATE])
    def run(self, params={}, state={}, custom_config={}):  # pylint: disable=unused-argument
        log_level = self.get_log_level(custom_config.get("log_level", "info"))
        self.connection.api.set_log_level(log_level)
        existing_state = state.copy()
        try:
            now_date = datetime.now(tz=timezone.utc).date()
            run_condition = self.detect_run_condition(state.get(QUERY_CONFIG, {}), now_date)
            self.logger.info(f"TASK: Run state is {run_condition}")
            state = self.update_state(state)
            page_size, thead_count, log_limit = self.apply_custom_config(state, run_condition, custom_config)
            furthest_lookback_date = self.get_furthest_lookback_date(state.get(QUERY_CONFIG, {}))
            max_run_lookback_date = self.get_max_lookback_date(
                now_date, run_condition, bool(custom_config), furthest_lookback_date
            )
            query_config = self.prepare_query_params(state.get(QUERY_CONFIG, {}), max_run_lookback_date, now_date)
            logs, query_config = self.get_all_logs(run_condition, query_config, page_size, thead_count, log_limit)
            exit_state, has_more_pages = self.prepare_exit_state(state, query_config, now_date, furthest_lookback_date)
            return logs, exit_state, has_more_pages, 200, None
        except APIException as error:
            self.logger.info(
                f"Error: An API exception has occurred. Status code: {error.status_code} returned. Cause: {error.cause}. Error data: {error.data}."
            )
            return [], existing_state, False, error.status_code, error
        except PluginException as error:
            self.logger.info(f"Error: A Plugin exception has occurred. Cause: {error.cause}  Error data: {error.data}.")
            return [], existing_state, False, 500, error
        except Exception as error:
            print(f"Error: Unknown exception has occurred. No results returned. Error Data: {error}")
            return (
                [],
                existing_state,
                False,
                500,
                PluginException(preset=PluginException.Preset.UNKNOWN, data=error),
            )

    def detect_run_condition(self, query_config: Dict, now_date: datetime) -> str:
        """
        Return runtype based on query configuration
        :param query_config:
        :param now_date:
        :return: runtype string
        """
        if not query_config:
            return INITIAL_RUN
        for log_type_config in query_config.values():
            if not log_type_config.get(CAUGHT_UP) or log_type_config.get(QUERY_DATE) not in str(now_date):
                return PAGINATION_RUN
        return SUBSEQUENT_RUN

    def get_furthest_lookback_date(self, query_config: Dict) -> datetime:
        """
        Get the furthest lookback date from the query configuration
        :param query_config:
        :return: furthest lookback date
        """
        furthest_date = None
        for config in query_config.values():
            if config.get(QUERY_DATE):
                log_date = datetime.strptime(config[QUERY_DATE], DATE_FORMAT).date()
                if furthest_date and log_date < furthest_date:
                    furthest_date = log_date
                elif not furthest_date:
                    furthest_date = log_date
        return furthest_date

    def update_state(self, state: Dict) -> Dict:
        """
        Initialise state, validate state, apply custom config
        :param state:
        :return: State
        """
        initial_log_type_config = {CAUGHT_UP: False}
        if not state:
            self.logger.info("TASK: Initializing first state...")
            state = {QUERY_CONFIG: {log_type: copy.deepcopy(initial_log_type_config) for log_type in LOG_TYPES}}
        else:
            for log_type in LOG_TYPES:
                if log_type not in state.get(QUERY_CONFIG, {}).keys():
                    self.logger.info(f"TASK: {log_type} missing from state. Initializing...")
                    state[QUERY_CONFIG][log_type] = copy.deepcopy(initial_log_type_config)
        return state

    def get_max_lookback_date(
        self,
        now_date: datetime,
        run_condition: str,
        custom_config: bool,
        last_query_date: datetime,
    ) -> datetime:
        """
        Get max lookback date for run condition
        :param now_date:
        :param run_condition:
        :param custom_config:
        :param last_query_date:
        :return: max_run_lookback_date
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

    def apply_custom_config(self, state: Dict, run_type: str, custom_config: Dict = {}) -> Tuple[int, int]:
        """
        Apply custom configuration for lookback, query date applies to start and end time of query
        :param state:
        :param current_query_config:
        :param run_type:
        :param custom_config:
        :return: Page size, thread count and log limit
        :return: Page size, thread count and log limits
        """
        custom_query_config = {}
        if custom_config:
            self.logger.info("TASK: Custom config detected")
            custom_query_config = custom_config.get("query_config", {})
        if run_type == INITIAL_RUN:
            current_query_config = state.get(QUERY_CONFIG)
            for log_type, log_query_config in custom_query_config.items():
                log_query_date = log_query_config.get("query_date", None)
                self.logger.info(f"TASK: Supplied lookback date of {log_query_date} for log type {log_type}")
                current_query_config[log_type] = {QUERY_DATE: log_query_date}
        page_size = max(1, min(custom_config.get(PAGE_SIZE, DEFAULT_PAGE_SIZE), DEFAULT_PAGE_SIZE))
        thread_count = max(1, custom_config.get(THREAD_COUNT, DEFAULT_THREAD_COUNT))
        log_limit = custom_config.get(LOG_LIMITS, {})
        return page_size, thread_count, log_limit

    def prepare_query_params(self, query_config: Dict, max_lookback_date: Dict, now_date: datetime) -> Dict:
        """
        Prepare query for request. Validate query dates, move forward when caught up
        :param query_config:
        :param max_lookback_date:
        :param now_date:
        :return:
        """
        for log_type, log_type_config in query_config.items():
            query_date = now_date
            query_date_str = log_type_config.get(QUERY_DATE)
            if query_date_str:
                query_date = datetime.strptime(query_date_str, DATE_FORMAT).date()
            if not query_date_str:
                self.logger.info(
                    f"TASK: Query date for {log_type} log type is not present. Initializing a {max_lookback_date}"
                )
                log_type_config[QUERY_DATE] = max_lookback_date
            elif query_date < now_date and log_type_config.get(CAUGHT_UP) is True:
                self.logger.info(f"TASK: Log type {log_type} has caught up for {query_date}")
                log_type_config[QUERY_DATE] = query_date + timedelta(days=1)
                log_type_config[CAUGHT_UP] = False
                log_type_config.pop(NEXT_PAGE)
            query_config[log_type] = self.validate_config_lookback(log_type_config, max_lookback_date, now_date)
        return query_config

    def validate_config_lookback(self, log_type_config: Dict, max_lookback_date: datetime, now_date: datetime) -> Dict:
        """
        Ensures provided query date in scope of request time window
        :param log_type_config:
        :param max_lookback_date:
        :param now_date:
        :return: log_type_config
        """
        query_date = log_type_config.get(QUERY_DATE)
        if isinstance(query_date, str):
            query_date = datetime.strptime(query_date, DATE_FORMAT).date()
        if query_date < max_lookback_date:
            return {QUERY_DATE: max_lookback_date}
        if query_date > now_date:
            log_type_config[QUERY_DATE] = now_date
        return log_type_config

    def get_all_logs(
        self,
        run_condition: str,
        query_config: Dict,
        page_size: int,
        thead_count: int,
        log_limits: Dict = {},
    ) -> Tuple[List, Dict]:
        """
        Gets all logs of provided log type. First retrieves batch URLs. Then downloads and reads batches, pooling logs.
        :param run_condition:
        :param query_config:
        :param page_size:
        :param thead_count:
        :param log_limit:
        :return: Logs, updated query configuration (state)
        """
        complete_logs = []
        for log_type, log_type_config in query_config.items():
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
                log_hash_size_limit = LARGE_LOG_HASH_SIZE_LIMIT if log_type == RECEIPT else SMALL_LOG_HASH_SIZE_LIMIT
                deduplicated_logs, log_hashes = self.compare_and_dedupe_hashes(
                    log_type_config.get(LOG_HASHES, []), logs, log_hash_size_limit
                )
                self.logger.info(
                    f"TASK: Number of logs after de-duplication: {len(deduplicated_logs)} for log type {log_type}"
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
                self.logger.info(f"TASK: Query for {log_type} is caught up. Skipping as we are currently paginating")
        return complete_logs, query_config

    def compare_and_dedupe_hashes(
        self,
        previous_logs_hashes: list,
        new_logs: list,
        log_hash_size_limit: int = SMALL_LOG_HASH_SIZE_LIMIT,
    ) -> Tuple[list, list]:
        """
        Iterate through two lists of values, hashing each. Compare hash value to a list of existing hash values.
        If the hash exists, return both it and the value in separate lists once iterated.
        :param previous_logs_hashes: List of existing hashes to compare against.
        :type list:
        :param new_logs: New values to hash and compare to existing list of hashes.
        :type list:
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
        :param state:
        :param query_config:
        :param now_date:
        :param furthest_query_date:
        :return: state, has_more_pages
        """
        has_more_pages = False
        for log_type_config in query_config.values():
            query_date = log_type_config.get(QUERY_DATE)
            if isinstance(query_date, str):
                query_date = datetime.strptime(query_date, DATE_FORMAT).date()
            if (not log_type_config.get(CAUGHT_UP)) or query_date < now_date:
                has_more_pages = True
            log_type_config[QUERY_DATE] = query_date.strftime(DATE_FORMAT)
        if furthest_query_date:
            furthest_query_date_str = furthest_query_date.strftime("%Y-%m-%d")
        else:
            furthest_query_date_str = None
        state[QUERY_CONFIG] = query_config
        state[FURTHEST_QUERY_DATE] = furthest_query_date_str
        return state, has_more_pages

    def get_log_level(self, log_level: str = "info") -> int:
        log_level_mappings = {
            "INFO": "DEBUG",  # we want to keep logging to a minimal so don't print our debug logs
            "DEBUG": "INFO",
            # we want to change loggers in this task to be of type "info" and included for traceability
        }

        return getLevelName(log_level_mappings.get(log_level.upper()))
