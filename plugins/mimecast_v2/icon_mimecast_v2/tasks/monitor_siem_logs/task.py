import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import APIException, PluginException
from .schema import MonitorSiemLogsInput, MonitorSiemLogsOutput, MonitorSiemLogsState, Input, Output, Component, State
from typing import Dict, Tuple
from datetime import datetime, timezone, timedelta


LOG_TYPES = ["receipt", "url protect", "attachment protect"]
INITIAL_STATE = {
    "receipt": {"caught_up": False},
    "url protect": {"caught_up": False},
    "attachment protect": {"caught_up": False},
}
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

    def run(self, params={}, state={}, custom_config={}):
        self.logger.info(f"TASK: Received State: {state}")
        existing_state = state.copy()
        try:
            run_condition = self.detect_run_condition(state)
            self.logger.info(f"TASK: Current run state is {run_condition}")
            now = datetime.now(tz=timezone.utc)
            now_date = now.date()
            max_api_lookback_date, max_run_lookback_date = self.get_max_lookback_date(
                now, run_condition, bool(custom_config)
            )
            if not state:
                state = INITIAL_STATE
                self.apply_custom_config(state, custom_config, max_api_lookback_date)
            query_config = self.prepare_query_params(state, max_run_lookback_date, now_date)
            logs, query_config = self.get_all_logs(run_condition, query_config)
            exit_state, has_more_pages = self.prepare_exit_state(query_config, now_date)
            return logs, exit_state, has_more_pages, 200, None
        except APIException as error:
            raise error
            self.logger.info(
                f"Error: An API exception has occurred. Status code: {error.status_code} returned. Cause: {error.cause}. Error data: {error.data}."
            )
            return [], existing_state, False, error.status_code, error
        except PluginException as error:
            raise error
            self.logger.info(f"Error: A Plugin exception has occurred. Cause: {error.cause}  Error data: {error.data}.")
            return [], existing_state, False, error.status_code, error
        except Exception as error:
            raise error
            self.logger.info(f"Error: Unknown exception has occurred. No results returned. Error Data: {error}")
            return [], existing_state, False, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def detect_run_condition(self, query_config: Dict) -> str:
        if not query_config:
            return INITIAL_RUN
        for log_type_config in query_config.values():
            if not log_type_config.get("caught_up"):
                return PAGINATION_RUN
        return SUBSEQUENT_RUN

    def get_max_lookback_date(self, now: datetime, run_condition: str, custom_config: bool):
        max_api_lookback_days = MAX_LOOKBACK_DAYS
        max_run_lookback_days = max_api_lookback_days
        if run_condition in [INITIAL_RUN] and not custom_config:
            max_run_lookback_days = INITIAL_MAX_LOOKBACK_DAYS

        max_api_lookback_date = (now - timedelta(days=max_api_lookback_days)).date()
        max_run_lookback_date = (now - timedelta(days=max_run_lookback_days)).date()
        return max_api_lookback_date, max_run_lookback_date

    def apply_custom_config(
        self, current_query_config: Dict, custom_config: Dict, max_lookback_date: datetime.date
    ) -> Dict:
        for log_type, lookback_date_string in custom_config.items():
            lookback_date = datetime.strptime(lookback_date_string, "%Y-%m-%d").date()
            if lookback_date > max_lookback_date:
                self.logger.info(f"TASK: Setting query date to {lookback_date} for {log_type} log type")
                current_query_config[log_type] = {"query_date": lookback_date_string}
            else:
                self.logger.info(
                    f"TASK: Supplied lookback date of {lookback_date} is beyond max lookback of {max_lookback_date} for {log_type} log type"
                )

    def prepare_query_params(self, query_config, max_lookback_date, now_date):
        for log_type, log_type_config in query_config.items():
            query_date_str = log_type_config.get("query_date")
            if query_date_str:
                query_date = datetime.strptime(query_date_str, "%Y-%m-%d").date()
            if not query_date_str:
                log_type_config["query_date"] = max_lookback_date
            elif query_date < now_date and log_type_config.get("caught_up") is True:
                self.logger.info(f"TASK: Log type {log_type} has caught up for {query_date}")
                log_type_config["query_date"] = query_date + timedelta(days=1)
                log_type_config["caught_up"] = False
                log_type_config.pop("next_page")
            query_config[log_type] = self.validate_config_lookback(log_type_config, max_lookback_date)
        return query_config

    def validate_config_lookback(self, log_type_config, max_lookback_date):
        if isinstance(log_type_config.get("query_date"), str):
            log_type_config["query_date"] = datetime.strptime(log_type_config["query_date"], "%Y-%m-%d").date()
        if log_type_config.get("query_date") < max_lookback_date:
            return {"query_date": max_lookback_date}
        return log_type_config

    def get_all_logs(self, run_condition: str, query_config: Dict):
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

    def prepare_exit_state(self, state, now_date) -> Tuple[Dict, bool]:
        has_more_pages = False
        for log_type, log_type_config in state.items():
            query_date = log_type_config.get("query_date")
            if log_type_config.get("caught_up") is True:
                has_more_pages = True
            if query_date:
                if query_date < now_date:
                    has_more_pages = True
                log_type_config["query_date"] = query_date.strftime("%Y-%m-%d")
        return state, has_more_pages
