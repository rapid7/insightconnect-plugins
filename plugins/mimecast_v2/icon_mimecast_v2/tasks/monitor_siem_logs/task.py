import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import APIException, PluginException
from insightconnect_plugin_runtime.helper import compare_and_dedupe_hashes, hash_sha1
from .schema import MonitorSiemLogsInput, MonitorSiemLogsOutput, MonitorSiemLogsState, Input, Output, Component, State
from typing import Dict, List, Tuple
from datetime import datetime, timezone, timedelta
import copy

# Date format for conversion
DATE_FORMAT = "%Y-%m-%d"
# Default and max values
LOG_TYPES = ["receipt", "url protect", "attachment protect"]
DEFAULT_THREAD_COUNT = 10
DEFAULT_PAGE_SIZE = 100
MAX_LOOKBACK_DAYS = 7
INITIAL_MAX_LOOKBACK_DAYS = 1
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
# Access keys for custom config
THREAD_COUNT = "thread_count"
PAGE_SIZE = "page_size"


class MonitorSiemLogs(insightconnect_plugin_runtime.Task):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_siem_logs",
            description=Component.DESCRIPTION,
            input=MonitorSiemLogsInput(),
            output=MonitorSiemLogsOutput(),
            state=MonitorSiemLogsState(),
        )

    def run(self, params={}, state={}, custom_config={}):  # pylint: disable=unused-argument
        self.logger.info(f"TASK: Received State: {state.get(QUERY_CONFIG)}")
        existing_state = state.copy()
        try:
            now_date = datetime.now(tz=timezone.utc).date()
            run_condition = self.detect_run_condition(state.get(QUERY_CONFIG, {}), now_date)
            self.logger.info(f"TASK: Run state is {run_condition}")
            state = self.update_state(state)
            page_size, thead_count = self.apply_custom_config(state, custom_config)
            max_run_lookback_date = self.get_max_lookback_date(now_date, run_condition, bool(custom_config))
            query_config = self.prepare_query_params(state.get(QUERY_CONFIG, {}), max_run_lookback_date, now_date)
            logs, query_config = self.get_all_logs(run_condition, query_config, page_size, thead_count)
            self.logger.info(f"TASK: Total logs collected this run {len(logs)}")
            logs, log_hashes = compare_and_dedupe_hashes(state.get(LOG_HASHES, []), logs)
            self.logger.info(f"TASK: Total logs after deduplication {len(logs)}")
            exit_state, has_more_pages = self.prepare_exit_state(state, query_config, now_date, log_hashes)
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
            self.logger.info(f"Error: Unknown exception has occurred. No results returned. Error Data: {error}")
            return [], existing_state, False, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

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

    def get_max_lookback_date(self, now_date: datetime, run_condition: str, custom_config: bool) -> datetime:
        """
        Get max lookback date for run condition
        :param now_date:
        :param run_condition:
        :param custom_config:
        :return: max_run_lookback_date
        """
        max_run_lookback_days = MAX_LOOKBACK_DAYS
        if run_condition in [INITIAL_RUN] and not custom_config:
            max_run_lookback_days = INITIAL_MAX_LOOKBACK_DAYS

        max_run_lookback_date = now_date - timedelta(days=max_run_lookback_days)
        return max_run_lookback_date

    def apply_custom_config(self, state: Dict, custom_config: Dict = {}) -> Tuple[int, int]:
        """
        Apply custom configuration for lookback, query date applies to start and end time of query
        :param current_query_config:
        :param custom_config:
        :return:
        """
        if custom_config:
            self.logger.info("TASK: Custom config detected")
        if not state:
            current_query_config = state.get(QUERY_CONFIG)
            for log_type, query_date_string in custom_config.items():
                self.logger.info(f"TASK: Supplied lookback date of {query_date_string} for log type {log_type}")
                current_query_config[log_type] = {QUERY_DATE: query_date_string}
        page_size = max(1, min(custom_config.get(PAGE_SIZE, DEFAULT_PAGE_SIZE), DEFAULT_PAGE_SIZE))
        thread_count = max(1, custom_config.get(THREAD_COUNT, DEFAULT_THREAD_COUNT))
        return page_size, thread_count

    def prepare_query_params(self, query_config: Dict, max_lookback_date: Dict, now_date: datetime) -> Dict:
        """
        Prepare query for request. Validate query dates, move forward when caught up
        :param query_config:
        :param max_lookback_date:
        :param now_date:
        :return:
        """
        for log_type, log_type_config in query_config.items():
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
        self, run_condition: str, query_config: Dict, page_size: int, thead_count: int
    ) -> Tuple[List, Dict]:
        """
        Gets all logs of provided log type. First retrieves batch URLs. Then downloads and reads batches, pooling logs.
        :param run_condition:
        :param query_config:
        :param page_size:
        :param thead_count:
        :return: Logs, updated query configuration (state)
        """
        complete_logs = []
        for log_type, log_type_config in query_config.items():
            if (not log_type_config.get(CAUGHT_UP)) or (run_condition != PAGINATION_RUN):
                logs, results_next_page, caught_up = self.connection.api.get_siem_logs(
                    log_type=log_type,
                    query_date=log_type_config.get(QUERY_DATE),
                    next_page=log_type_config.get(NEXT_PAGE),
                    page_size=page_size,
                    max_threads=thead_count,
                )
                complete_logs.extend(logs)
                log_type_config.update({NEXT_PAGE: results_next_page, CAUGHT_UP: caught_up})
            else:
                self.logger.info(f"TASK: Query for {log_type} is caught up. Skipping as we are currently paginating")
        return complete_logs, query_config

    def prepare_exit_state(
        self, state: dict, query_config: dict, now_date: datetime, log_hashes: List[str]
    ) -> Tuple[Dict, bool]:
        """
        Prepare state and pagination for task completion. Format date time.
        :param state:
        :param query_config:
        :param now_date:
        :param log_hashes:
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
        state[QUERY_CONFIG] = query_config
        state[LOG_HASHES] = log_hashes
        return state, has_more_pages
