import insightconnect_plugin_runtime
from .schema import MonitorLogsInput, MonitorLogsOutput, MonitorLogsState, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from datetime import datetime, timedelta, timezone
from komand_okta.util.helpers import clean
import re


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
        if not state:
            self.logger.info("First run")
            now = self.get_current_time()
            last_24_hours = now - timedelta(hours=24)
            parameters = {"since": last_24_hours.isoformat(), "until": now.isoformat(), "limit": 1000}
            state["last_collection_timestamp"] = now.isoformat()
        else:
            self.logger.info("Subsequent run")
            now = self.get_current_time().isoformat()
            parameters = {"since": state.get("last_collection_timestamp"), "until": now, "limit": 1000}
            state["last_collection_timestamp"] = now
        try:
            new_logs = self.connection.api_client.get_all_pages(self.connection.api_client.list_events(parameters))
            state["status_code"] = 200
            return clean(new_logs), state, None
        except PluginException as error:
            state["status_code"] = self.extract_status_code(error.data)
            return [], state, None

    @staticmethod
    def get_current_time():
        return datetime.now(timezone.utc)

    @staticmethod
    def extract_status_code(error):
        split_error = error.split("\n")
        status_code = re.search(r"\d{3}", split_error[0])
        return int(status_code.group()) if status_code else 500
