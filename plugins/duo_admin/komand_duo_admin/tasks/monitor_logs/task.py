from typing import Dict

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import MonitorLogsInput, MonitorLogsOutput, MonitorLogsState, Component, Input

# Custom imports below
from komand_duo_admin.util.exceptions import ApiException
from datetime import datetime, timedelta, timezone
from hashlib import sha1

ADMIN_LOGS_LOG_TYPE = "Admin logs"
AUTH_LOGS_LOG_TYPE = "Auth logs"
TRUST_MONITOR_EVENTS_LOG_TYPE = "Trust monitor events"
CUTOFF_HOURS = 24
MAX_CUTOFF_HOURS = 72


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
            filter_time = self._get_filter_time(custom_config, now, CUTOFF_HOURS)
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
            # Need to ensure that no more than the previous 3 days is queried - use cutoff check to ensure this
            # Prevent resuming of task from previous timestamp if beyond 3 days resulting in large data collection
            max_cutoff_time = self._get_filter_time(custom_config, now, MAX_CUTOFF_HOURS)
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
                if log_type == "Admin logs":
                    # Use seconds for admin log endpoint
                    mintime = max(last_log_timestamp, cutoff_time_secs)
                    maxtime = self.convert_to_seconds(last_two_minutes)
                else:
                    if log_type == AUTH_LOGS_LOG_TYPE:
                        # New method holds logmtimestamps in seconds so convert to milliseconds for auth logs
                        last_log_timestamp_millisecs = int(last_log_timestamp * 1000)
                    else:
                        # Trust monitor events hold timestamps in milliseconds(surface_timestamp is recorded)
                        last_log_timestamp_millisecs = last_log_timestamp
                    mintime = max(last_log_timestamp_millisecs, cutoff_time_millisecs)
                    maxtime = self.convert_to_milliseconds(last_two_minutes)

        self.logger.info(f"Retrieve data from {mintime} to {maxtime}. Get next page is set to {get_next_page}")
        return mintime, maxtime, get_next_page

    def run(self, params={}, state={}, custom_config={}):  # noqa: C901
        self.connection.admin_api.toggle_rate_limiting = False
        has_more_pages = False
        backward_comp_first_run = False
        try:
            now = self.get_current_time()
            last_collection_timestamp = state.get(self.LAST_COLLECTION_TIMESTAMP)
            trust_monitor_next_page_params = state.get(self.TRUST_MONITOR_NEXT_PAGE_PARAMS)
            auth_logs_next_page_params = state.get(self.AUTH_LOGS_NEXT_PAGE_PARAMS)
            admin_logs_next_page_params = state.get(self.ADMIN_LOGS_NEXT_PAGE_PARAMS)
            collect_trust_monitor_events = params.get(Input.COLLECTTRUSTMONITOREVENTS, True)
            collect_admin_logs = params.get(Input.COLLECTADMINLOGS, True)

            if last_collection_timestamp:
                # Previously only one timestamp was held (the end of the collection window)
                # This has been superceded by a latest timestamp per log type
                self.logger.info(
                    f"Backwards compatibility - update all timestamps to the last known timestamp {last_collection_timestamp}"
                )
                trust_monitor_last_log_timestamp = (
                    auth_logs_last_log_timestamp
                ) = admin_logs_last_log_timestamp = last_collection_timestamp
                # Update the old last collection timestamp to None so it is not considered in future runs
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
            try:
                new_logs = []
                previous_trust_monitor_event_hashes = state.get(self.PREVIOUS_TRUST_MONITOR_EVENT_HASHES, [])
                previous_admin_log_hashes = state.get(self.PREVIOUS_ADMIN_LOG_HASHES, [])
                previous_auth_log_hashes = state.get(self.PREVIOUS_AUTH_LOG_HASHES, [])
                new_trust_monitor_event_hashes, new_admin_log_hashes, new_auth_log_hashes = [], [], []

                if collect_trust_monitor_events:
                    # Get trust monitor events
                    mintime, maxtime, get_next_page = self.get_parameters_for_query(
                        TRUST_MONITOR_EVENTS_LOG_TYPE,
                        now,
                        trust_monitor_last_log_timestamp,
                        trust_monitor_next_page_params,
                        backward_comp_first_run,
                        custom_config,
                    )

                    if (get_next_page and trust_monitor_next_page_params) or not get_next_page:
                        trust_monitor_events, trust_monitor_next_page_params = self.get_trust_monitor_event(
                            mintime, maxtime, trust_monitor_next_page_params
                        )
                        new_trust_monitor_events, new_trust_monitor_event_hashes = self.compare_hashes(
                            previous_trust_monitor_event_hashes, trust_monitor_events
                        )
                        new_logs.extend(new_trust_monitor_events)
                        state[self.TRUST_MONITOR_LAST_LOG_TIMESTAMP] = self.get_highest_timestamp(
                            trust_monitor_last_log_timestamp,
                            new_trust_monitor_events,
                            backward_comp_first_run,
                            TRUST_MONITOR_EVENTS_LOG_TYPE,
                        )
                        self.logger.info(f"{len(new_trust_monitor_events)} trust monitor events retrieved")
                    if new_trust_monitor_event_hashes:
                        state[self.PREVIOUS_TRUST_MONITOR_EVENT_HASHES] = new_trust_monitor_event_hashes

                    if trust_monitor_next_page_params:
                        state[self.TRUST_MONITOR_NEXT_PAGE_PARAMS] = trust_monitor_next_page_params
                        has_more_pages = True
                    elif state.get(self.TRUST_MONITOR_NEXT_PAGE_PARAMS):
                        state.pop(self.TRUST_MONITOR_NEXT_PAGE_PARAMS)
                else:
                    self.logger.info(
                        f"Collect trust monitor events set to {collect_trust_monitor_events}. Do not attempt to collect trust monitor events"
                    )

                if collect_admin_logs:
                    # Get admin logs
                    mintime, maxtime, get_next_page = self.get_parameters_for_query(
                        ADMIN_LOGS_LOG_TYPE,
                        now,
                        admin_logs_last_log_timestamp,
                        admin_logs_next_page_params,
                        backward_comp_first_run,
                        custom_config,
                    )

                    if (get_next_page and admin_logs_next_page_params) or not get_next_page:
                        admin_logs, admin_logs_next_page_params = self.get_admin_logs(
                            mintime, maxtime, admin_logs_next_page_params
                        )
                        new_admin_logs, new_admin_log_hashes = self.compare_hashes(
                            previous_admin_log_hashes, admin_logs
                        )
                        new_logs.extend(new_admin_logs)
                        state[self.ADMIN_LOGS_LAST_LOG_TIMESTAMP] = self.get_highest_timestamp(
                            admin_logs_last_log_timestamp, new_admin_logs, backward_comp_first_run, ADMIN_LOGS_LOG_TYPE
                        )
                        self.logger.info(f"{len(new_admin_logs)} admin logs retrieved")

                    if new_admin_log_hashes:
                        state[self.PREVIOUS_ADMIN_LOG_HASHES] = new_admin_log_hashes
                    if admin_logs_next_page_params:
                        state[self.ADMIN_LOGS_NEXT_PAGE_PARAMS] = admin_logs_next_page_params
                        has_more_pages = True
                    elif state.get(self.ADMIN_LOGS_NEXT_PAGE_PARAMS):
                        state.pop(self.ADMIN_LOGS_NEXT_PAGE_PARAMS)
                else:
                    self.logger.info(
                        f"Collect admin logs set to {collect_admin_logs}. Do not attempt to collect admin logs"
                    )

                # Get auth logs
                mintime, maxtime, get_next_page = self.get_parameters_for_query(
                    AUTH_LOGS_LOG_TYPE,
                    now,
                    auth_logs_last_log_timestamp,
                    auth_logs_next_page_params,
                    backward_comp_first_run,
                    custom_config,
                )

                if (get_next_page and auth_logs_next_page_params) or not get_next_page:
                    auth_logs, auth_logs_next_page_params = self.get_auth_logs(
                        mintime, maxtime, auth_logs_next_page_params
                    )
                    new_auth_logs, new_auth_log_hashes = self.compare_hashes(previous_auth_log_hashes, auth_logs)
                    # Grab the most recent timestamp and save it to use as min time for next run
                    new_logs.extend(new_auth_logs)
                    state[self.AUTH_LOGS_LAST_LOG_TIMESTAMP] = self.get_highest_timestamp(
                        auth_logs_last_log_timestamp, new_auth_logs, backward_comp_first_run, AUTH_LOGS_LOG_TYPE
                    )
                    self.logger.info(f"{len(new_auth_logs)} auth logs retrieved")

                if new_auth_log_hashes:
                    state[self.PREVIOUS_AUTH_LOG_HASHES] = new_auth_log_hashes

                if auth_logs_next_page_params:
                    state[self.AUTH_LOGS_NEXT_PAGE_PARAMS] = auth_logs_next_page_params
                    has_more_pages = True
                elif state.get(self.AUTH_LOGS_NEXT_PAGE_PARAMS):
                    state.pop(self.AUTH_LOGS_NEXT_PAGE_PARAMS)

                return new_logs, state, has_more_pages, 200, None
            except ApiException as error:
                self.logger.info(f"An API Exception has been raised. Status code: {error.status_code}. Error: {error}")
                state[self.PREVIOUS_TRUST_MONITOR_EVENT_HASHES] = []
                state[self.PREVIOUS_ADMIN_LOG_HASHES] = []
                state[self.PREVIOUS_AUTH_LOG_HASHES] = []
                return [], state, False, error.status_code, error
        except Exception as error:
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

    @staticmethod
    def add_log_type_field(logs: list, value: str) -> list:
        for log in logs:
            log["log_type"] = value
        return logs

    @staticmethod
    def sha1(log: dict) -> str:
        hash_ = sha1()  # nosec B303
        for key, value in log.items():
            hash_.update(f"{key}{value}".encode("utf-8"))
        return hash_.hexdigest()

    def compare_hashes(self, previous_logs_hashes: list, new_logs: list):
        new_logs_hashes = []
        logs_to_return = []
        for log in new_logs:
            hash_ = self.sha1(log)
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
        self.logger.info(f"Response returned from get trust monitor events: {response}")
        offset = response.get("metadata", {}).get("next_offset")
        if offset:
            parameters["offset"] = offset
        else:
            parameters = {}
        trust_monitor_events = self.add_log_type_field(response.get("events", []), "trust_monitor_event")
        return trust_monitor_events, parameters

    def _get_filter_time(self, custom_config: Dict, current_time: datetime, default_hours: int) -> int:
        """
        Apply custom_config params (if provided) to the task. If a lookback value exists, it should take
        precedence (this can allow a larger filter time), otherwise use the cutoff_hours value.
        :param custom_config: dictionary passed containing `cutoff` or `lookback` values
        :param current_time: Datetime of now
        :param default_hours: integer value representing default cutoff hours
        :return: filter_value (epoch seconds) to be applied in request to Duo
        """
        filter_cutoff = custom_config.get("cutoff", {}).get("date")
        if filter_cutoff is None:
            filter_cutoff = custom_config.get("cutoff", {}).get("hours", default_hours)
        filter_lookback = custom_config.get("lookback")
        filter_value = filter_lookback if filter_lookback else filter_cutoff
        # If CUTOFF_HOURS (hours in int) applied find date time from now
        if isinstance(filter_value, int):
            filter_value = current_time - timedelta(hours=filter_value)
        else:
            filter_value = datetime.fromisoformat(filter_value.replace("Z", "+00:00"))
        self.logger.info(f"Task execution will be applying a lookback to {filter_value}...")
        return filter_value
