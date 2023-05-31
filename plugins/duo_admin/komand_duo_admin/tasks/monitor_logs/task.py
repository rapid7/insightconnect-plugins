import insightconnect_plugin_runtime
from .schema import MonitorLogsInput, MonitorLogsOutput, MonitorLogsState, Component

# Custom imports below
from komand_duo_admin.util.exceptions import ApiException
from datetime import datetime, timedelta, timezone
from insightconnect_plugin_runtime.helper import convert_dict_to_camel_case
from komand_duo_admin.util.helpers import clean, convert_fields_to_string
from hashlib import sha1


class MonitorLogs(insightconnect_plugin_runtime.Task):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_logs",
            description=Component.DESCRIPTION,
            input=MonitorLogsInput(),
            output=MonitorLogsOutput(),
            state=MonitorLogsState(),
        )

    def run(self, params={}, state={}):  # pylint: disable=unused-argument
        now = self.get_current_time()
        last_minute = now - timedelta(minutes=1)
        last_collection_timestamp = state.get("last_collection_timestamp")
        if not last_collection_timestamp:
            self.logger.info("First run")
            last_24_hours = now - timedelta(hours=24)
            mintime_in_milliseconds = self.convert_to_milliseconds(last_24_hours)
            maxtime_in_milliseconds = self.convert_to_milliseconds(last_minute)
            mintime_in_seconds = self.convert_to_seconds(last_24_hours)
            maxtime_in_seconds = self.convert_to_seconds(last_minute)
        else:
            self.logger.info("Subsequent run")
            mintime_in_milliseconds = last_collection_timestamp
            maxtime_in_milliseconds = self.convert_to_milliseconds(last_minute)
            mintime_in_seconds = int(mintime_in_milliseconds / 1000)
            maxtime_in_seconds = int(maxtime_in_milliseconds / 1000)
        try:
            new_logs = []
            state["last_collection_timestamp"] = maxtime_in_milliseconds
            new_logs.extend(self.get_auth_logs(mintime_in_milliseconds, maxtime_in_milliseconds))
            new_logs.extend(self.get_admin_logs(mintime_in_seconds, maxtime_in_seconds))
            new_logs.extend(self.get_trust_monitor_event(mintime_in_milliseconds, maxtime_in_milliseconds))
            state["status_code"] = 200
            new_logs = self.remove_duplicates(clean(new_logs))

            previous_logs_hashes = state.get("previous_logs_hashes")
            new_logs_hashes = []
            logs_to_return = []
            if previous_logs_hashes:
                for log in new_logs:
                    hash_ = self.sha1(log)
                    if hash_ not in previous_logs_hashes:
                        new_logs_hashes.append(hash_)
                        logs_to_return.append(log)
            else:
                logs_to_return = new_logs
                for log in new_logs:
                    new_logs_hashes.append(self.sha1(log))

            state["previous_logs_hashes"] = new_logs_hashes
            return logs_to_return, state, None
        except ApiException as error:
            state["status_code"] = error.status_code
            state["previous_logs_hashes"] = []
            return [], state, None

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
    def remove_duplicates(logs: list) -> list:
        logs_to_return = []
        for log in logs:
            if log not in logs_to_return:
                logs_to_return.append(log)
        return logs_to_return

    @staticmethod
    def sha1(log: dict) -> str:
        hash_ = sha1()
        for key, value in log.items():
            hash_.update(f"{key}{value}".encode("utf-8"))
        return hash_.hexdigest()

    def get_auth_logs(self, mintime: int, maxtime: int) -> list:
        parameters = {"mintime": str(mintime), "maxtime": str(maxtime), "limit": str(1000)}
        auth_logs = self.add_log_type_field(self.connection.admin_api.get_all_auth_logs(parameters), "authentication")
        return convert_fields_to_string(convert_dict_to_camel_case(clean(auth_logs)))

    def get_admin_logs(self, mintime: int, maxtime: int) -> list:
        parameters = {"mintime": str(mintime)}
        admin_logs = self.add_log_type_field(
            self.connection.admin_api.get_all_admin_logs(parameters, maxtime), "administrator"
        )
        return convert_dict_to_camel_case(clean(admin_logs))

    def get_trust_monitor_event(self, mintime: int, maxtime: int) -> list:
        parameters = {"mintime": str(mintime), "maxtime": str(maxtime), "limit": str(200)}
        trust_monitor_events = self.add_log_type_field(
            self.connection.admin_api.get_all_trust_monitor_events(parameters), "trust_monitor_event"
        )
        return convert_dict_to_camel_case(clean(trust_monitor_events))
