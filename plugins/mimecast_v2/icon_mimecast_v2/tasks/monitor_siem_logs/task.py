import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import APIException, PluginException
from .schema import MonitorSiemLogsInput, MonitorSiemLogsOutput, MonitorSiemLogsState, Input, Output, Component, State
from typing import Dict, List, Tuple
from datetime import datetime, timezone, timedelta
import copy

LOG_TYPES = ["receipt", "url protect", "attachment protect"]
MAX_LOOKBACK_DAYS = 7
INITIAL_MAX_LOOKBACK_DAYS = 1
INITIAL_RUN = "initial_run"
SUBSEQUENT_RUN = "subsequent_run"
PAGINATION_RUN = "pagination_run"


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
        self.logger.info(f"TASK: Received State: {state}")
        existing_state = state.copy()
        try:
            # TODO: Additional error handling
            run_condition = self.detect_run_condition(state.get("query_config", {}))
            self.logger.info(f"TASK: Current run state is {run_condition}")
            state = self.update_state(state, custom_config)
            self.logger.info(f"NEW STATE: {state}")
            now_date = datetime.now(tz=timezone.utc).date()
            max_run_lookback_date = self.get_max_lookback_date(now_date, run_condition, bool(custom_config))
            query_config = self.prepare_query_params(state.get("query_config", {}), max_run_lookback_date, now_date)
            logs, query_config = self.get_all_logs(run_condition, query_config)
            # TODO: Dedupe
            self.logger.info(f"TASK: Total logs collected this run {len(logs)}")
            exit_state, has_more_pages = self.prepare_exit_state(state, query_config, now_date)
            return logs, exit_state, has_more_pages, 200, None
        except APIException as error:
            self.logger.info(
                f"Error: An API exception has occurred. Status code: {error.status_code} returned. Cause: {error.cause}. Error data: {error.data}."
            )
            return [], existing_state, False, error.status_code, error
        except PluginException as error:
            self.logger.info(f"Error: A Plugin exception has occurred. Cause: {error.cause}  Error data: {error.data}.")
            return [], existing_state, False, error.status_code, error
        except Exception as error:
            self.logger.info(f"Error: Unknown exception has occurred. No results returned. Error Data: {error}")
            return [], existing_state, False, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def detect_run_condition(self, query_config: Dict) -> str:
        """
        Return runtype based on query configuration
        :param query_config:
        :return: runtype string
        """
        if not query_config:
            return INITIAL_RUN
        for log_type_config in query_config.values():
            if not log_type_config.get("caught_up"):
                return PAGINATION_RUN
        return SUBSEQUENT_RUN

    def update_state(self, state: Dict, custom_config: Dict) -> Dict:
        """
        Initialise state, validate state, apply custom config
        :param state:
        :param custom_config:
        :return:
        """
        initial_log_type_config = {"caught_up": False}
        if not state:
            state = {"query_config": {log_type: copy.deepcopy(initial_log_type_config) for log_type in LOG_TYPES}}
            self.apply_custom_config(state, custom_config)
        else:
            for log_type in LOG_TYPES:
                if log_type not in state.get("query_config", {}).keys():
                    state["query_config"][log_type] = copy.deepcopy(initial_log_type_config)
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

    def apply_custom_config(self, state: Dict, custom_config: Dict) -> None:
        """
        Apply custom configuration for lookback, query date applies to start and end time of query
        :param current_query_config:
        :param custom_config:
        :return: N/A
        """
        # TODO: Additional custom config for page size, thread size, limit
        current_query_config = state.get("query_config")
        for log_type, lookback_date_string in custom_config.items():
            self.logger.info(f"TASK: Supplied lookback date of {lookback_date_string} for {log_type} log type")
            current_query_config[log_type] = {"query_date": lookback_date_string}

    def prepare_query_params(self, query_config: Dict, max_lookback_date: Dict, now_date: datetime) -> Dict:
        """
        Prepare query for request. Validate query dates, move forward when caught up
        :param query_config:
        :param max_lookback_date:
        :param now_date:
        :return:
        """
        for log_type, log_type_config in query_config.items():
            query_date_str = log_type_config.get("query_date")
            self.logger.info(f"PREPPING {log_type_config}")
            self.logger.info(f"{log_type}, {query_date_str}")
            if query_date_str:
                query_date = datetime.strptime(query_date_str, "%Y-%m-%d").date()
            if not query_date_str:
                log_type_config["query_date"] = max_lookback_date
            elif query_date < now_date and log_type_config.get("caught_up") is True:
                self.logger.info(f"TASK: Log type {log_type} has caught up for {query_date}")
                log_type_config["query_date"] = query_date + timedelta(days=1)
                log_type_config["caught_up"] = False
                log_type_config.pop("next_page")
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
        query_date = log_type_config.get("query_date")
        if isinstance(query_date, str):
            query_date = datetime.strptime(query_date, "%Y-%m-%d").date()
        if query_date < max_lookback_date:
            return {"query_date": max_lookback_date}
        if query_date > now_date:
            log_type_config["query_date"] = now_date
        return log_type_config

    def get_all_logs(self, run_condition: str, query_config: Dict) -> Tuple[List, Dict]:
        """
        Gets all logs of provided log type. First retrieves batch URLs. Then downloads and reads batches, pooling logs.
        :param run_condition:
        :param query_config:
        :return: Logs, updated query configuration (state)
        """
        complete_logs = []
        for log_type, log_type_config in query_config.items():
            if (not log_type_config.get("caught_up")) or (run_condition != PAGINATION_RUN):
                logs, results_next_page, caught_up = self.connection.api.get_siem_logs(
                    log_type=log_type,
                    query_date=log_type_config.get("query_date"),
                    next_page=log_type_config.get("next_page"),
                )
                complete_logs.extend(logs)
                log_type_config.update({"next_page": results_next_page, "caught_up": caught_up})
            else:
                self.logger.info(f"TASK: Query for {log_type} is caught up. Skipping as we are currently paginating")
        return complete_logs, query_config

    def prepare_exit_state(self, state: dict, query_config: dict, now_date: datetime) -> Tuple[Dict, bool]:
        """
        Prepare state and pagination for task completion. Format date time.
        :param state:
        :param query_config:
        :param now_date:
        :return: state, has_more_pages
        """
        has_more_pages = False
        for log_type_config in query_config.values():
            query_date = log_type_config.get("query_date")
            if isinstance(query_date, str):
                query_date = datetime.strptime(query_date, "%Y-%m-%d").date()
            if (not log_type_config.get("caught_up")) or query_date < now_date:
                has_more_pages = True
            log_type_config["query_date"] = query_date.strftime("%Y-%m-%d")
        state["query_config"] = query_config
        return state, has_more_pages
