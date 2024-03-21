import insightconnect_plugin_runtime
from .schema import RerunReportInput, RerunReportOutput, Input, Component, Output


class RerunReport(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="rerun_report",
            description=Component.DESCRIPTION,
            input=RerunReportInput(),
            output=RerunReportOutput(),
        )

    def run(self, params={}):
        task_id = params.get(Input.TASK_ID, "")
        endpoint = f"tasks/rereport/{task_id}"
        response = self.connection.api.send(endpoint)
        return {Output.SUCCESS: response.get("success")}
