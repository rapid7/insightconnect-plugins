from datetime import datetime, timedelta, timezone
from time import time
from typing import Any, Dict, Tuple, Union

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import hash_sha1
from insightconnect_plugin_runtime.telemetry import monitor_task_delay

# Custom imports below
from komand_duo_admin.util.constants import Assistance
from komand_duo_admin.util.exceptions import ApiException
from komand_duo_admin.util.util import Utils
from komand_duo_admin.util.helpers import convert_string_to_bool

from .schema import MonitorLogsInput, MonitorLogsOutput, MonitorLogsState, Component, Input

ADMIN_LOGS_LOG_TYPE = "Admin logs"
AUTH_LOGS_LOG_TYPE = "Auth logs"
TRUST_MONITOR_EVENTS_LOG_TYPE = "Trust monitor events"
INITIAL_CUTOFF_HOURS = 24
MAX_CUTOFF_HOURS = 168
API_CUTOFF_HOURS = 4320
RATE_LIMIT_DELAY = 600


class MonitorLogs(insightconnect_plugin_runtime.Task):
    LAST_COLLECTION_TIMESTAMP = "last_collection_timestamp"
    ADMIN_LOGS_LAST_LOG_TIMESTAMP = "admin_logs_last_log_timestamp"
    AUTH_LOGS_LAST_LOG_TIMESTAMP = "auth_logs_last_log_timestamp"
    TRUST_MONITOR_LAST_LOG_TIMESTAMP = "trust_monitor_last_log_timestamp"
    STATUS_CODE = "status_code"
    ADMIN_LOGS_NEXT_PAGE_PARAMS = "admin_logs_next_page_params"
    AUTH_LOGS_NEXT_PAGE_PARAMS = "auth_logs_next_page_params"
    TRUST_MONITOR_NEXT_PAGE_PARAMS = "trust_monitor_next_page_params"
    PREVIOUS_ADMIN_LOG_HASHES = "previous_admin_log_hashes"
    PREVIOUS_AUTH_LOG_HASHES = "previous_auth_log_hashes"
    PREVIOUS_TRUST_MONITOR_EVENT_HASHES = "previous_trust_monitor_event_hashes"
    RATE_LIMIT_DATETIME = "rate_limit_datetime"

    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_logs",
            description=Component.DESCRIPTION,
            input=MonitorLogsInput(),
            output=MonitorLogsOutput(),
            state=MonitorLogsState(),
        )

    def get_parameters_for_query(
        self, log_type, now, last_log_timestamp, next_page_params, backward_comp_first_run, custom_config
    ):
        get_next_page = False
        last_two_minutes = now - timedelta(minutes=2)
        # If no previous timestamp retrieved (first run) then query 24 hours
        if not last_log_timestamp:
            self.logger.info(f"First run for {log_type}")
            filter_time = self._get_filter_time(custom_config, now, INITIAL_CUTOFF_HOURS, log_type)
            if log_type != "Admin logs":
                mintime = self.convert_to_milliseconds(filter_time)
                maxtime = self.convert_to_milliseconds(last_two_minutes)
            else:
                # Use seconds for admin log endpoint
                mintime = self.convert_to_seconds(filter_time)
                maxtime = self.convert_to_seconds(last_two_minutes)
        # Else if a previous timestamp was retrieved (subsequent runs) then query to that timestamp
        else:
            if next_page_params:
                self.logger.info("Getting the next page of results...")
                get_next_page = True
            else:
                self.logger.info(f"Subsequent run for {log_type}")

            # If for some reason no logs or event have been picked up,
            # Need to ensure that no more than the previous 7 days is queried - use cutoff check to ensure this
            # Prevent resuming of task from previous timestamp if beyond 7 days resulting in large data collection
            max_cutoff_time = self._get_filter_time(custom_config, now, MAX_CUTOFF_HOURS, log_type, last_log_timestamp)
            cutoff_time_secs = self.convert_to_seconds(max_cutoff_time)
            cutoff_time_millisecs = self.convert_to_milliseconds(max_cutoff_time)
            if backward_comp_first_run:
                # This is a special case where the previous last collection timestamp needs to change to 3 different
                # timestamps getting held. Once all systems are updated to 3 timestamp method, remove this clause
                # Note: The last collection timestamp is held in milliseconds,
                # new timestamps are in seconds. (10 digit unix integer)
                self.logger.info("Backward compatibility - adjust times from last collection timestamp")
                if log_type != "Admin logs":
                    # Timestamps in milliseconds, original timestamp method held timestamp in milliseconds
                    mintime = max(last_log_timestamp, cutoff_time_millisecs)
                    maxtime = self.convert_to_milliseconds(last_two_minutes)
                else:
                    # Use seconds for admin log endpoint
                    last_log_timestamp_secs = int(last_log_timestamp / 1000)
                    mintime = max(last_log_timestamp_secs, cutoff_time_secs)
                    maxtime = self.convert_to_seconds(last_two_minutes)
            else:
                if log_type == ADMIN_LOGS_LOG_TYPE:
                    # Use seconds for admin log endpoint
                    mintime = max(last_log_timestamp, cutoff_time_secs)
                    maxtime = self.convert_to_seconds(last_two_minutes)
                else:
                    if log_type == AUTH_LOGS_LOG_TYPE:
                        # New method holds log time stamps in seconds so convert to milliseconds for auth logs
                        last_log_timestamp_millisecs = int(last_log_timestamp * 1000)
                    else:
                        # Trust monitor events hold timestamps in milliseconds(surface_timestamp is recorded)
                        last_log_timestamp_millisecs = last_log_timestamp
                    mintime = max(last_log_timestamp_millisecs, cutoff_time_millisecs)
                    maxtime = self.convert_to_milliseconds(last_two_minutes)

        self.logger.info(f"Retrieve data from {mintime} to {maxtime}. Get next page is set to {get_next_page}")
        return mintime, maxtime, get_next_page

    def check_rate_limit(self, state: Dict) -> Union[PluginException, None]:
        rate_limited = state.get(self.RATE_LIMIT_DATETIME)
        now = time()
        if rate_limited:
            rate_limit_string = Utils.convert_epoch_to_readable(rate_limited)
            log_msg = f"Rate limit value stored in state: {rate_limit_string}. "
            if rate_limited > now:
                log_msg += "Still within rate limiting period, skipping task execution..."
                self.logger.info(log_msg)
                error = PluginException(
                    cause=PluginException.causes.get(PluginException.Preset.RATE_LIMIT),
                    assistance=Assistance.RATE_LIMIT,
                )
                return error

            log_msg += "However no longer in rate limiting period, so task can be executed..."
            del state[self.RATE_LIMIT_DATETIME]
            self.logger.info(log_msg)

    def check_rate_limit_error(
        self, error: ApiException, status_code: int, state: dict, rate_limit_delay: int
    ) -> Tuple[int, Any]:
        if status_code == 429:
            new_run_time = time() + rate_limit_delay  # default to wait 10 minutes before the next run
            try:
                new_run_time_string = Utils.convert_epoch_to_readable(new_run_time)
                self.logger.error(f"A rate limit error has occurred, task will resume after {new_run_time_string}")
                state[self.RATE_LIMIT_DATETIME] = new_run_time
            except Exception as err:
                self.logger.error(
                    f"Unable to calculate new run time, no rate limiting applied to the state. Error: {repr(err)}",
                    exc_info=True,
                )
            return 200, None
        return status_code, error

    # pylint: disable=too-many-branches,too-many-statements
    @monitor_task_delay(
        timestamp_keys=[
            "admin_logs_last_log_timestamp",
            "auth_logs_last_log_timestamp",
            "trust_monitor_last_log_timestamp",
        ],
        default_delay_threshold="2d",
    )  # noqa: C901
    def run(self, params={}, state={}, custom_config={}):  # noqa: C901
        rate_limit_delay = custom_config.get("rate_limit_delay", RATE_LIMIT_DELAY)
        if rate_limited := self.check_rate_limit(state):
            return [], state, False, 429, rate_limited
        self.connection.admin_api.toggle_rate_limiting = False
        has_more_pages = False
        try:
            now = self.get_current_time()
            (
                trust_monitor_last_log_timestamp,
                auth_logs_last_log_timestamp,
                admin_logs_last_log_timestamp,
                backward_comp_first_run,
            ) = self._handle_backward_compatibility(state)
            trust_monitor_next_page_params = state.get(self.TRUST_MONITOR_NEXT_PAGE_PARAMS)
            auth_logs_next_page_params = state.get(self.AUTH_LOGS_NEXT_PAGE_PARAMS)
            admin_logs_next_page_params = state.get(self.ADMIN_LOGS_NEXT_PAGE_PARAMS)
            collect_trust_monitor_events = convert_string_to_bool(params.get(Input.COLLECTTRUSTMONITOREVENTS, True))
            collect_admin_logs = convert_string_to_bool(params.get(Input.COLLECTADMINLOGS, True))

            new_logs = []

            # Trust monitor events
            if collect_trust_monitor_events:
                (
                    new_logs,
                    state,
                    has_more_pages,
                ) = self._collect_log_type(
                    log_type=TRUST_MONITOR_EVENTS_LOG_TYPE,
                    now=now,
                    last_log_timestamp=trust_monitor_last_log_timestamp,
                    next_page_params=trust_monitor_next_page_params,
                    backward_comp_first_run=backward_comp_first_run,
                    custom_config=custom_config,
                    previous_hashes=state.get(self.PREVIOUS_TRUST_MONITOR_EVENT_HASHES, []),
                    state=state,
                    state_last_log_key=self.TRUST_MONITOR_LAST_LOG_TIMESTAMP,
                    state_hashes_key=self.PREVIOUS_TRUST_MONITOR_EVENT_HASHES,
                    state_next_page_key=self.TRUST_MONITOR_NEXT_PAGE_PARAMS,
                    new_logs=new_logs,
                    has_more_pages=has_more_pages,
                    get_logs_func=self.get_trust_monitor_event,
                    compare_hashes_func=self.compare_hashes,
                    get_highest_timestamp_func=self.get_highest_timestamp,
                    log_label="trust monitor events",
                )
            else:
                self.logger.info(
                    f"Collect trust monitor events set to {collect_trust_monitor_events}. Do not attempt to collect trust monitor events"
                )

            # Admin logs
            if collect_admin_logs:
                (
                    new_logs,
                    state,
                    has_more_pages,
                ) = self._collect_log_type(
                    log_type=ADMIN_LOGS_LOG_TYPE,
                    now=now,
                    last_log_timestamp=admin_logs_last_log_timestamp,
                    next_page_params=admin_logs_next_page_params,
                    backward_comp_first_run=backward_comp_first_run,
                    custom_config=custom_config,
                    previous_hashes=state.get(self.PREVIOUS_ADMIN_LOG_HASHES, []),
                    state=state,
                    state_last_log_key=self.ADMIN_LOGS_LAST_LOG_TIMESTAMP,
                    state_hashes_key=self.PREVIOUS_ADMIN_LOG_HASHES,
                    state_next_page_key=self.ADMIN_LOGS_NEXT_PAGE_PARAMS,
                    new_logs=new_logs,
                    has_more_pages=has_more_pages,
                    get_logs_func=self.get_admin_logs,
                    compare_hashes_func=self.compare_hashes,
                    get_highest_timestamp_func=self.get_highest_timestamp,
                    log_label="admin logs",
                )
            else:
                self.logger.info(
                    f"Collect admin logs set to {collect_admin_logs}. Do not attempt to collect admin logs"
                )

            # Auth logs (always collected)
            (
                new_logs,
                state,
                has_more_pages,
            ) = self._collect_log_type(
                log_type=AUTH_LOGS_LOG_TYPE,
                now=now,
                last_log_timestamp=auth_logs_last_log_timestamp,
                next_page_params=auth_logs_next_page_params,
                backward_comp_first_run=backward_comp_first_run,
                custom_config=custom_config,
                previous_hashes=state.get(self.PREVIOUS_AUTH_LOG_HASHES, []),
                state=state,
                state_last_log_key=self.AUTH_LOGS_LAST_LOG_TIMESTAMP,
                state_hashes_key=self.PREVIOUS_AUTH_LOG_HASHES,
                state_next_page_key=self.AUTH_LOGS_NEXT_PAGE_PARAMS,
                new_logs=new_logs,
                has_more_pages=has_more_pages,
                get_logs_func=self.get_auth_logs,
                compare_hashes_func=self.compare_hashes,
                get_highest_timestamp_func=self.get_highest_timestamp,
                log_label="auth logs",
            )

            return new_logs, state, has_more_pages, 200, None

        except ApiException as error:
            return self._handle_api_exception(error, state, rate_limit_delay)
        except Exception as error:
            return self._handle_general_exception(error, state, has_more_pages)

    def _handle_backward_compatibility(self, state):
        last_collection_timestamp = state.get(self.LAST_COLLECTION_TIMESTAMP)
        if last_collection_timestamp:
            self.logger.info(
                f"Backwards compatibility - update all timestamps to the last known timestamp {last_collection_timestamp}"
            )
            trust_monitor_last_log_timestamp = auth_logs_last_log_timestamp = admin_logs_last_log_timestamp = (
                last_collection_timestamp
            )
            state[self.LAST_COLLECTION_TIMESTAMP] = None
            backward_comp_first_run = True
        else:
            trust_monitor_last_log_timestamp = state.get(self.TRUST_MONITOR_LAST_LOG_TIMESTAMP)
            auth_logs_last_log_timestamp = state.get(self.AUTH_LOGS_LAST_LOG_TIMESTAMP)
            admin_logs_last_log_timestamp = state.get(self.ADMIN_LOGS_LAST_LOG_TIMESTAMP)
            self.logger.info(
                f"Previous timestamps retrieved. "
                f"Auth {auth_logs_last_log_timestamp}. "
                f"Admin: {admin_logs_last_log_timestamp}. "
                f"Trust monitor {trust_monitor_last_log_timestamp}."
            )
            backward_comp_first_run = False
        return (
            trust_monitor_last_log_timestamp,
            auth_logs_last_log_timestamp,
            admin_logs_last_log_timestamp,
            backward_comp_first_run,
        )

    def _collect_log_type(
        self,
        log_type,
        now,
        last_log_timestamp,
        next_page_params,
        backward_comp_first_run,
        custom_config,
        previous_hashes,
        state,
        state_last_log_key,
        state_hashes_key,
        state_next_page_key,
        new_logs,
        has_more_pages,
        get_logs_func,
        compare_hashes_func,
        get_highest_timestamp_func,
        log_label,
    ):
        mintime, maxtime, get_next_page = self.get_parameters_for_query(
            log_type,
            now,
            last_log_timestamp,
            next_page_params,
            backward_comp_first_run,
            custom_config,
        )
        if (get_next_page and next_page_params) or not get_next_page:
            logs, next_params = get_logs_func(mintime, maxtime, next_page_params)
            new_logs_list, new_hashes = compare_hashes_func(previous_hashes, logs)
            new_logs.extend(new_logs_list)
            self.logger.info(f"{len(new_logs_list)} {log_label} retrieved")
            if new_hashes:
                state[state_hashes_key] = new_hashes
                state[state_last_log_key] = get_highest_timestamp_func(
                    last_log_timestamp, new_logs_list, backward_comp_first_run, log_type
                )
            else:
                state[state_last_log_key] = maxtime
            if next_params:
                state[state_next_page_key] = next_params
                has_more_pages = True
            elif state.get(state_next_page_key):
                state.pop(state_next_page_key)
        return new_logs, state, has_more_pages

    def _handle_api_exception(self, error, state, rate_limit_delay):
        self.logger.info(f"An API Exception has been raised. Status code: {error.status_code}. Error: {error}")
        state[self.PREVIOUS_TRUST_MONITOR_EVENT_HASHES] = []
        state[self.PREVIOUS_ADMIN_LOG_HASHES] = []
        state[self.PREVIOUS_AUTH_LOG_HASHES] = []
        status_code, error = self.check_rate_limit_error(error, error.status_code, state, rate_limit_delay)
        return [], state, False, status_code, error

    def _handle_general_exception(self, error, state, has_more_pages):
        self.logger.info(f"An Exception has been raised. Error: {error}")
        state[self.PREVIOUS_TRUST_MONITOR_EVENT_HASHES] = []
        state[self.PREVIOUS_ADMIN_LOG_HASHES] = []
        state[self.PREVIOUS_AUTH_LOG_HASHES] = []
        return [], state, has_more_pages, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    @staticmethod
    def get_current_time():
        return datetime.now(timezone.utc)

    @staticmethod
    def convert_to_milliseconds(date_time) -> int:
        return int(date_time.timestamp() * 1000)

    @staticmethod
    def convert_to_seconds(date_time) -> int:
        return int(date_time.timestamp())

    def convert_epoch_to_datetime(self, epoch_timestamp: int) -> datetime:
        """
        Convert an epoch timestamp to a datetime object.

        :param epoch_timestamp: The epoch timestamp to convert (in milliseconds or seconds).
        :return: A datetime object representing the epoch timestamp.
        """

        # Ensure the epoch timestamp is an integer. If not, attempt to convert it.
        if not isinstance(epoch_timestamp, int):
            self.logger.debug(
                f"The epoch timestamp is not an integer: {epoch_timestamp} - type ({type(epoch_timestamp)}). Attempting to convert it to an integer."
            )
            epoch_timestamp = int(epoch_timestamp)

        try:
            # Try to convert the epoch timestamp assuming it's in seconds
            return datetime.utcfromtimestamp(epoch_timestamp).replace(tzinfo=timezone.utc)
        except ValueError:
            # If it fails, assume it's in milliseconds and convert accordingly
            return datetime.utcfromtimestamp(epoch_timestamp / 1000).replace(tzinfo=timezone.utc)

    @staticmethod
    def add_log_type_field(logs: list, value: str) -> list:
        for log in logs:
            log["log_type"] = value
        return logs

    def compare_hashes(self, previous_logs_hashes: list, new_logs: list):
        new_logs_hashes = []
        logs_to_return = []
        for log in new_logs:
            hash_ = hash_sha1(log)
            if hash_ not in previous_logs_hashes:
                new_logs_hashes.append(hash_)
                logs_to_return.append(log)
        self.logger.info(
            f"Original number of logs:{len(new_logs)}. Number of logs after de-duplication:{len(logs_to_return)}"
        )
        return logs_to_return, new_logs_hashes

    def get_highest_timestamp(self, last_recorded_highest_timestamp, logs, backward_comp_first_run, log_type):
        if last_recorded_highest_timestamp:
            if backward_comp_first_run:
                # Convert the previous timestamp (13 digit format) to the new format used
                # (Timestamps now held in the last log timestamp format which is a 10 digit unix timestamp)
                # Note trust monitor events maintain the surfaced_timestamp which is 13 digit unix timestamp
                self.logger.info("Ensure backward compatibility (to older one timestamp method)")
                if log_type != TRUST_MONITOR_EVENTS_LOG_TYPE:
                    last_recorded_highest_timestamp = int(last_recorded_highest_timestamp / 1000)
            highest_timestamp = last_recorded_highest_timestamp
        else:
            highest_timestamp = 0
        self.logger.info(f"Previous highest recorded timestamp is {highest_timestamp}")
        for log in logs:
            # Event monitor uses surfaced_timestamp but other endpoints use timestamp
            if log_type == TRUST_MONITOR_EVENTS_LOG_TYPE:
                log_timestamp = log.get("surfaced_timestamp")
            else:
                log_timestamp = log.get("timestamp")
            if log_timestamp and log_timestamp > highest_timestamp:
                highest_timestamp = log_timestamp
        self.logger.info(f"Highest timestamp set to {highest_timestamp} for {log_type}")
        return highest_timestamp

    def get_auth_logs(self, mintime: int, maxtime: int, next_page_params: dict) -> list:
        self.logger.info(f"Get auth logs: mintime:{mintime}, maxtime:{maxtime}, next_page_params:{next_page_params}")
        parameters = (
            next_page_params
            if next_page_params
            else {"mintime": str(mintime), "maxtime": str(maxtime), "limit": str(1000)}
        )
        parameters.update({"sort": "ts:asc"})
        self.logger.info(f"Parameters for get auth logs set to {parameters}")
        response = self.connection.admin_api.get_auth_logs(parameters).get("response", {})
        metadata = response.get("metadata") or {}
        next_offset = metadata.get("next_offset")
        if next_offset:
            parameters["next_offset"] = ",".join(next_offset)
        else:
            parameters = {}
        auth_logs = self.add_log_type_field(response.get("authlogs", []), "authentication")
        self.logger.info(f"Get auth logs: parameters to return {parameters}. Return {len(auth_logs)} logs")
        return auth_logs, parameters

    def get_admin_logs(self, mintime: int, maxtime: int, next_page_params: dict) -> list:
        self.logger.info(f"Get admin logs: mintime:{mintime}, maxtime:{maxtime}, next_page_params:{next_page_params}")
        parameters = {"mintime": next_page_params.get("mintime") if next_page_params else str(mintime)}
        self.logger.info(f"Parameters for get admin logs set to {parameters}")
        response = self.connection.admin_api.get_admin_logs(parameters).get("response", [])
        last_item = response[-1] if response and isinstance(response, list) else None

        if last_item and len(response) == 1000:
            parameters = {"mintime": str(last_item.get("timestamp")), "maxtime": maxtime}
        else:
            parameters = {}

        logs_to_return = []
        for log in response:
            if log.get("timestamp") <= maxtime:
                logs_to_return.append(log)

        admin_logs = self.add_log_type_field(logs_to_return, "administrator")
        self.logger.info(f"Parameters to return from get admin logs set to {parameters}. Return {len(admin_logs)} logs")
        return admin_logs, parameters

    def get_trust_monitor_event(self, mintime: int, maxtime: int, next_page_params: dict) -> list:
        parameters = (
            next_page_params
            if next_page_params
            else {"mintime": str(mintime), "maxtime": str(maxtime), "limit": str(200)}
        )
        self.logger.info(f"Parameters for get trust monitor events set to {parameters}")
        response = self.connection.admin_api.get_trust_monitor_events(parameters).get("response", {})
        self.logger.info(
            f"Parameters to return from trust monitor events set to {parameters}. "
            f"Return {len(response.get('events', []))} events"
        )
        offset = response.get("metadata", {}).get("next_offset")
        if offset:
            parameters["offset"] = offset
        else:
            parameters = {}
        trust_monitor_events = self.add_log_type_field(response.get("events", []), "trust_monitor_event")
        return trust_monitor_events, parameters

    def _get_filter_time(
        self,
        custom_config: Dict,
        current_time: datetime,
        default_hours: int,
        log_type: str = None,
        last_log_timestamp: any = None,
    ) -> datetime:
        """
        Apply custom_config params (if provided) to the task. If a lookback value exists for that task type, it should
        take precedence (this can allow a larger filter time), otherwise use the cutoff_hours value.
        :param custom_config: dictionary passed containing `cutoff` or `lookback` values
        :param current_time: Datetime of now
        :param default_hours: integer value representing default cutoff hours
        :param log_type: Log type value to be used to determine which lookback to retrieve from custom_config
        :param last_log_timestamp: Last log timestamp to be used for lookback
        :return: filter_value (epoch seconds) to be applied in request to Duo
        """
        log_types = {
            AUTH_LOGS_LOG_TYPE: "filter_cutoff_auth_logs",
            ADMIN_LOGS_LOG_TYPE: "filter_cutoff_admin_logs",
            TRUST_MONITOR_EVENTS_LOG_TYPE: "filter_cutoff_trust_monitor_events_logs",
        }
        filter_cutoff = custom_config.get(log_types.get(log_type, ""), {}).get("date")
        if filter_cutoff is None:
            # If no values retrieved, use log_type.hours from custom_config
            # If no log_type.hours, then use default_hours
            filter_cutoff = custom_config.get(log_types.get(log_type, ""), {}).get("hours", default_hours)
        filter_lookback = custom_config.get("lookback")
        filter_value = filter_lookback if filter_lookback else filter_cutoff
        # If CUTOFF_HOURS (hours in int) applied find date time from now
        if isinstance(filter_value, int):
            filter_value = current_time - timedelta(hours=filter_value)
        else:
            filter_value = datetime.fromisoformat(filter_value.replace("Z", "+00:00"))
        # Compare lookback value to API cutoff value, applying API cutoff if lookback is beyond API limits
        utc_filter_value = filter_value.astimezone(timezone.utc)
        api_cutoff_date = current_time - timedelta(hours=API_CUTOFF_HOURS)
        if api_cutoff_date > utc_filter_value:
            self.logger.info(
                f"Lookback of {utc_filter_value} is older than 180 days. Looking back to {api_cutoff_date}..."
            )
            utc_filter_value = api_cutoff_date
        # Check if last_log_timestamp is within 7 days and if it is then use that as the lookback value
        if last_log_timestamp:
            last_log_datetime = self.convert_epoch_to_datetime(last_log_timestamp)
            utc_filter_value = max(utc_filter_value, last_log_datetime)
        self.logger.info(f"Task execution for {log_type} will be applying a lookback to {utc_filter_value} UTC...")
        return utc_filter_value
