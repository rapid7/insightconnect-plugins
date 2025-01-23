import insightconnect_plugin_runtime
from .schema import MonitorSiemLogsInput, MonitorSiemLogsOutput, MonitorSiemLogsState, Input, Output, Component, State
# Custom imports below


class MonitorSiemLogs(insightconnect_plugin_runtime.Task):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="monitor_siem_logs",
                description=Component.DESCRIPTION,
                input=MonitorSiemLogsInput(),
                output=MonitorSiemLogsOutput(),
                state=MonitorSiemLogsState())

    def run(self, params={}, state={}):
        # TODO: Implement run function
        return {}, {}
