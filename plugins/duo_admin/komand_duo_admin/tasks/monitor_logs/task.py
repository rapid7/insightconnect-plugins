import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import MonitorLogsInput, MonitorLogsOutput, MonitorLogsState, Component

# Custom imports below
from komand_duo_admin.util.exceptions import ApiException
from datetime import datetime, timedelta, timezone
from hashlib import sha1


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

    def get_parameters_for_query(self, log_type, now, last_log_timestamp, next_page_params):
        get_next_page = False
        last_two_minutes = now - timedelta(minutes=2)
        if not last_log_timestamp:
            self.logger.info(f"First run for {log_type}")
            last_24_hours = now - timedelta(hours=24)
            if log_type != "admin_logs":
                mintime = self.convert_to_milliseconds(last_24_hours)
                maxtime = self.convert_to_milliseconds(last_two_minutes)
            else:
                # Use seconds for admin log endpoint
                mintime = self.convert_to_seconds(last_24_hours)
                maxtime = self.convert_to_seconds(last_two_minutes)

        else:
            if next_page_params:
                self.logger.info("Getting the next page of results...")
                get_next_page = True
            else:
                self.logger.info(f"Subsequent run for {log_type}")
            if log_type != "admin_logs":
                mintime = last_log_timestamp
                maxtime = self.convert_to_milliseconds(last_two_minutes)
            else:
                # Use seconds for admin log endpoint
                mintime = int(last_log_timestamp / 1000)
                maxtime = self.convert_to_seconds(last_two_minutes)

        self.logger.info(f"Retrieve data from {mintime} to {maxtime}. Get next page is set to {get_next_page}")
        return mintime, maxtime, get_next_page

    # pylint: disable=unused-argument
    def run(self, params={}, state={}):  # noqa: C901
        self.connection.admin_api.toggle_rate_limiting = False
        has_more_pages = False

        try:
            now = self.get_current_time()
            last_collection_timestamp = state.get(self.LAST_COLLECTION_TIMESTAMP)
            trust_monitor_next_page_params = state.get(self.TRUST_MONITOR_NEXT_PAGE_PARAMS)
            auth_logs_next_page_params = state.get(self.AUTH_LOGS_NEXT_PAGE_PARAMS)
            admin_logs_next_page_params = state.get(self.ADMIN_LOGS_NEXT_PAGE_PARAMS)

            if last_collection_timestamp:
                # Previously only one timestamp was held (the end of the collection window)
                # This has been superceded by a latest timestamp per log type
                self.logger.info("Backwards compatibility - update all timestamps to the last known timestamp")
                trust_monitor_last_log_timestamp = auth_logs_last_log_timestamp = admin_logs_last_log_timestamp = last_collection_timestamp
                # Update the old last collection timestamp to None so it is not considered in future runs
                state[self.LAST_COLLECTION_TIMESTAMP] = None
            else:
                trust_monitor_last_log_timestamp = state.get(self.TRUST_MONITOR_LAST_LOG_TIMESTAMP)
                auth_logs_last_log_timestamp = state.get(self.AUTH_LOGS_LAST_LOG_TIMESTAMP)
                admin_logs_last_log_timestamp = state.get(self.ADMIN_LOGS_LAST_LOG_TIMESTAMP)
                self.logger.info(f"Previous timestamps retrieved. "
                                 f"Auth {auth_logs_last_log_timestamp} "
                                 f"Admin: {admin_logs_last_log_timestamp}. "
                                 f"Trust monitor {trust_monitor_last_log_timestamp}")
            try:
                new_logs = []

                previous_trust_monitor_event_hashes = state.get(self.PREVIOUS_TRUST_MONITOR_EVENT_HASHES, [])
                previous_admin_log_hashes = state.get(self.PREVIOUS_ADMIN_LOG_HASHES, [])
                previous_auth_log_hashes = state.get(self.PREVIOUS_AUTH_LOG_HASHES, [])

                new_trust_monitor_event_hashes = new_admin_log_hashes = new_auth_log_hashes =[]

                # Get trust monitor events
                mintime, maxtime, get_next_page = self.get_parameters_for_query("Trust monitor events",
                                                                                now, trust_monitor_last_log_timestamp,
                                                                                trust_monitor_next_page_params)

                if (get_next_page and trust_monitor_next_page_params) or not get_next_page:
                    trust_monitor_events, trust_monitor_next_page_params = self.get_trust_monitor_event(
                        mintime, maxtime, trust_monitor_next_page_params
                    )
                    new_trust_monitor_events, new_trust_monitor_event_hashes = self.compare_hashes(
                        previous_trust_monitor_event_hashes, trust_monitor_events
                    )
                    new_logs.extend(new_trust_monitor_events)
                    state[self.TRUST_MONITOR_LAST_LOG_TIMESTAMP] = self.get_highest_timestamp(new_trust_monitor_events)
                    self.logger.info(f"{len(new_trust_monitor_events)} trust monitor events retrieved")
                state[self.PREVIOUS_TRUST_MONITOR_EVENT_HASHES] = (
                    previous_trust_monitor_event_hashes
                    if not new_trust_monitor_event_hashes and get_next_page
                    else new_trust_monitor_event_hashes
                )
                if trust_monitor_next_page_params:
                    state[self.TRUST_MONITOR_NEXT_PAGE_PARAMS] = trust_monitor_next_page_params
                    has_more_pages = True
                elif state.get(self.TRUST_MONITOR_NEXT_PAGE_PARAMS):
                    state.pop(self.TRUST_MONITOR_NEXT_PAGE_PARAMS)

                # Get admin logs
                mintime, maxtime, get_next_page = self.get_parameters_for_query("Admin logs", now,
                                                                                admin_logs_last_log_timestamp,
                                                                                admin_logs_next_page_params)

                if (get_next_page and admin_logs_next_page_params) or not get_next_page:
                    admin_logs, admin_logs_next_page_params = self.get_admin_logs(
                        mintime, maxtime, admin_logs_next_page_params
                    )
                    new_admin_logs, new_admin_log_hashes = self.compare_hashes(previous_admin_log_hashes, admin_logs)
                    new_logs.extend(new_admin_logs)
                    state[self.ADMIN_LOGS_LAST_LOG_TIMESTAMP] = self.get_highest_timestamp(new_admin_logs)
                    self.logger.info(f"{len(new_admin_logs)} admin logs retrieved")
                state[self.PREVIOUS_ADMIN_LOG_HASHES] = (
                    previous_admin_log_hashes if not new_admin_log_hashes and get_next_page else new_admin_log_hashes
                )

                if admin_logs_next_page_params:
                    state[self.ADMIN_LOGS_NEXT_PAGE_PARAMS] = admin_logs_next_page_params
                    has_more_pages = True
                elif state.get(self.ADMIN_LOGS_NEXT_PAGE_PARAMS):
                    state.pop(self.ADMIN_LOGS_NEXT_PAGE_PARAMS)

                # Get auth logs
                mintime, maxtime, get_next_page = self.get_parameters_for_query("Auth logs", now,
                                                                                auth_logs_last_log_timestamp,
                                                                                auth_logs_next_page_params)
                if (get_next_page and auth_logs_next_page_params) or not get_next_page:
                    auth_logs, auth_logs_next_page_params = self.get_auth_logs(
                        mintime, maxtime, auth_logs_next_page_params
                    )
                    new_auth_logs, new_auth_log_hashes = self.compare_hashes(previous_auth_log_hashes, auth_logs)
                    # Grab the most recent timestamp and save it to use as min time for next run
                    new_logs.extend(new_auth_logs)
                    state[self.AUTH_LOGS_LAST_LOG_TIMESTAMP] = self.get_highest_timestamp(new_auth_logs)
                    self.logger.info(f"{len(new_auth_logs)} auth logs retrieved")
                state[self.PREVIOUS_AUTH_LOG_HASHES] = (
                    previous_auth_log_hashes if not new_auth_log_hashes and get_next_page else new_auth_log_hashes
                )
                if auth_logs_next_page_params:
                    state[self.AUTH_LOGS_NEXT_PAGE_PARAMS] = auth_logs_next_page_params
                    has_more_pages = True
                elif state.get(self.AUTH_LOGS_NEXT_PAGE_PARAMS):
                    state.pop(self.AUTH_LOGS_NEXT_PAGE_PARAMS)

                return new_logs, state, has_more_pages, 200, None
            except ApiException as error:
                state[self.PREVIOUS_TRUST_MONITOR_EVENT_HASHES] = []
                state[self.PREVIOUS_ADMIN_LOG_HASHES] = []
                state[self.PREVIOUS_AUTH_LOG_HASHES] = []
                return [], state, False, error.status_code, error
        except Exception as error:
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
        return logs_to_return, new_logs_hashes

    def get_highest_timestamp(self, logs):
        highest_timestamp = 0
        for log in logs:
            log_timestamp = log.get("timestamp")
            if log_timestamp and log_timestamp > highest_timestamp:
                highest_timestamp = log_timestamp
        self.logger.info(f"Highest timestamp set to {highest_timestamp}")
        return highest_timestamp


    def get_auth_logs(self, mintime: int, maxtime: int, next_page_params: dict) -> list:
        parameters = (
            next_page_params
            if next_page_params
            else {"mintime": str(mintime), "maxtime": str(maxtime), "limit": str(1000)}
        )
        parameters.update("sort", "asc")
        self.logger.info(f"Parameters for get auth logs set to {parameters}")
        response = self.connection.admin_api.get_auth_logs(parameters).get("response", {})
        metadata = response.get("metadata") or {}
        next_offset = metadata.get("next_offset")
        if next_offset:
            parameters["next_offset"] = ",".join(next_offset)
        else:
            parameters = {}
        auth_logs = self.add_log_type_field(response.get("authlogs", []), "authentication")
        return auth_logs, parameters

    def get_admin_logs(self, mintime: int, maxtime: int, next_page_params: dict) -> list:
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
        return admin_logs, parameters

    def get_trust_monitor_event(self, mintime: int, maxtime: int, next_page_params: dict) -> list:
        parameters = (
            next_page_params
            if next_page_params
            else {"mintime": str(mintime), "maxtime": str(maxtime), "limit": str(200)}
        )
        self.logger.info(f"Parameters for get trust monitor events set to {parameters}")
        response = self.connection.admin_api.get_trust_monitor_events(parameters).get("response", {})
        offset = response.get("metadata", {}).get("next_offset")
        if offset:
            parameters["offset"] = offset
        else:
            parameters = {}
        trust_monitor_events = self.add_log_type_field(response.get("events", []), "trust_monitor_event")
        return trust_monitor_events, parameters
