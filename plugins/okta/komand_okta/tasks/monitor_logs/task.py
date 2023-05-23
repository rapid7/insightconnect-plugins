import insightconnect_plugin_runtime
from .schema import MonitorLogsInput, MonitorLogsOutput, MonitorLogsState, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_okta.util.exceptions import ApiException
from datetime import datetime, timedelta, timezone
from komand_okta.util.helpers import clean


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
        except ApiException as error:
            state["status_code"] = error.status_code
            return [], state, None

    @staticmethod
    def get_current_time():
        return datetime.now(timezone.utc)
