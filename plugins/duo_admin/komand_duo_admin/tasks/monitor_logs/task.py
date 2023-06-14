import insightconnect_plugin_runtime
from .schema import MonitorLogsInput, MonitorLogsOutput, MonitorLogsState, Component

# Custom imports below
from komand_duo_admin.util.exceptions import ApiException
from datetime import datetime, timedelta, timezone
from insightconnect_plugin_runtime.helper import convert_dict_to_camel_case
from komand_duo_admin.util.helpers import clean, convert_fields_to_string
from hashlib import sha1


class MonitorLogs(insightconnect_plugin_runtime.Task):
    LAST_COLLECTION_TIMESTAMP = "last_collection_timestamp"
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

    # pylint: disable=unused-argument
    def run(self, params={}, state={}):  # noqa: C901
        now = self.get_current_time()
        last_minute = now - timedelta(minutes=1)
        last_collection_timestamp = state.get(self.LAST_COLLECTION_TIMESTAMP)

        has_more_pages = False
        get_next_page = False
        trust_monitor_next_page_params = state.get(self.TRUST_MONITOR_NEXT_PAGE_PARAMS)
        auth_logs_next_page_params = state.get(self.AUTH_LOGS_NEXT_PAGE_PARAMS)
        admin_logs_next_page_params = state.get(self.ADMIN_LOGS_NEXT_PAGE_PARAMS)

        if not last_collection_timestamp:
            self.logger.info("First run")
            last_24_hours = now - timedelta(hours=24)
            mintime_in_milliseconds = self.convert_to_milliseconds(last_24_hours)
            maxtime_in_milliseconds = self.convert_to_milliseconds(last_minute)
            mintime_in_seconds = self.convert_to_seconds(last_24_hours)
            maxtime_in_seconds = self.convert_to_seconds(last_minute)
        else:
            if trust_monitor_next_page_params or auth_logs_next_page_params or admin_logs_next_page_params:
                self.logger.info("Getting the next page of results...")
                get_next_page = True
            else:
                self.logger.info("Subsequent run")
            mintime_in_milliseconds = last_collection_timestamp
            maxtime_in_milliseconds = self.convert_to_milliseconds(last_minute)
            mintime_in_seconds = int(mintime_in_milliseconds / 1000)
            maxtime_in_seconds = int(maxtime_in_milliseconds / 1000)
        try:
            new_logs = []
            if not get_next_page:
                state[self.LAST_COLLECTION_TIMESTAMP] = maxtime_in_milliseconds

            previous_trust_monitor_event_hashes = state.get(self.PREVIOUS_TRUST_MONITOR_EVENT_HASHES, [])
            previous_admin_log_hashes = state.get(self.PREVIOUS_ADMIN_LOG_HASHES, [])
            previous_auth_log_hashes = state.get(self.PREVIOUS_AUTH_LOG_HASHES, [])
            new_trust_monitor_event_hashes = []
            new_admin_log_hashes = []
            new_auth_log_hashes = []

            if (get_next_page and trust_monitor_next_page_params) or not get_next_page:
                trust_monitor_events, trust_monitor_next_page_params = self.get_trust_monitor_event(
                    mintime_in_milliseconds, maxtime_in_milliseconds, trust_monitor_next_page_params
                )
                new_trust_monitor_events, new_trust_monitor_event_hashes = self.compare_hashes(
                    previous_trust_monitor_event_hashes, trust_monitor_events
                )
                new_logs.extend(new_trust_monitor_events)
            if (get_next_page and admin_logs_next_page_params) or not get_next_page:
                admin_logs, admin_logs_next_page_params = self.get_admin_logs(
                    mintime_in_seconds, maxtime_in_seconds, admin_logs_next_page_params
                )
                new_admin_logs, new_admin_log_hashes = self.compare_hashes(previous_admin_log_hashes, admin_logs)
                new_logs.extend(new_admin_logs)
            if (get_next_page and auth_logs_next_page_params) or not get_next_page:
                auth_logs, auth_logs_next_page_params = self.get_auth_logs(
                    mintime_in_milliseconds, maxtime_in_milliseconds, auth_logs_next_page_params
                )
                new_auth_logs, new_auth_log_hashes = self.compare_hashes(previous_auth_log_hashes, auth_logs)
                new_logs.extend(new_auth_logs)

            state[self.PREVIOUS_TRUST_MONITOR_EVENT_HASHES] = (
                previous_trust_monitor_event_hashes
                if not new_trust_monitor_event_hashes and get_next_page
                else new_trust_monitor_event_hashes
            )
            state[self.PREVIOUS_ADMIN_LOG_HASHES] = (
                previous_admin_log_hashes if not new_admin_log_hashes and get_next_page else new_admin_log_hashes
            )
            state[self.PREVIOUS_AUTH_LOG_HASHES] = (
                previous_auth_log_hashes if not new_auth_log_hashes and get_next_page else new_auth_log_hashes
            )
            state[self.STATUS_CODE] = 200

            if trust_monitor_next_page_params:
                state[self.TRUST_MONITOR_NEXT_PAGE_PARAMS] = trust_monitor_next_page_params
                has_more_pages = True
            elif state.get(self.TRUST_MONITOR_NEXT_PAGE_PARAMS):
                state.pop(self.TRUST_MONITOR_NEXT_PAGE_PARAMS)
            if auth_logs_next_page_params:
                state[self.AUTH_LOGS_NEXT_PAGE_PARAMS] = auth_logs_next_page_params
                has_more_pages = True
            elif state.get(self.AUTH_LOGS_NEXT_PAGE_PARAMS):
                state.pop(self.AUTH_LOGS_NEXT_PAGE_PARAMS)
            if admin_logs_next_page_params:
                state[self.ADMIN_LOGS_NEXT_PAGE_PARAMS] = admin_logs_next_page_params
                has_more_pages = True
            elif state.get(self.ADMIN_LOGS_NEXT_PAGE_PARAMS):
                state.pop(self.ADMIN_LOGS_NEXT_PAGE_PARAMS)

            return new_logs, state, has_more_pages
        except ApiException as error:
            state[self.STATUS_CODE] = error.status_code
            state[self.PREVIOUS_TRUST_MONITOR_EVENT_HASHES] = []
            state[self.PREVIOUS_ADMIN_LOG_HASHES] = []
            state[self.PREVIOUS_AUTH_LOG_HASHES] = []
            return [], state, False

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
            log["logType"] = value
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

    def get_auth_logs(self, mintime: int, maxtime: int, next_page_params: dict) -> list:
        parameters = (
            next_page_params
            if next_page_params
            else {"mintime": str(mintime), "maxtime": str(maxtime), "limit": str(1000)}
        )
        response = self.connection.admin_api.get_auth_logs(parameters).get("response", {})
        next_offset = response.get("metadata", {}).get("next_offset")
        if next_offset:
            parameters["next_offset"] = next_offset
        else:
            parameters = {}
        auth_logs = self.add_log_type_field(response.get("authlogs", []), "authentication")
        return convert_fields_to_string(convert_dict_to_camel_case(clean(auth_logs))), parameters

    def get_admin_logs(self, mintime: int, maxtime: int, next_page_params: dict) -> list:
        parameters = {"mintime": next_page_params.get("mintime") if next_page_params else str(mintime)}
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
        return convert_dict_to_camel_case(clean(admin_logs)), parameters

    def get_trust_monitor_event(self, mintime: int, maxtime: int, next_page_params: dict) -> list:
        parameters = (
            next_page_params
            if next_page_params
            else {"mintime": str(mintime), "maxtime": str(maxtime), "limit": str(200)}
        )
        response = self.connection.admin_api.get_trust_monitor_events(parameters).get("response", {})
        offset = response.get("metadata", {}).get("next_offset")
        if offset:
            parameters["offset"] = offset
        else:
            parameters = {}
        trust_monitor_events = self.add_log_type_field(response.get("events", []), "trust_monitor_event")
        return convert_dict_to_camel_case(clean(trust_monitor_events)), parameters
