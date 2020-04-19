import insightconnect_plugin_runtime
from .schema import GetReportInput, GetReportOutput, Input, Output, Component
# Custom imports below


class GetReport(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_report',
                description=Component.DESCRIPTION,
                input=GetReportInput(),
                output=GetReportOutput())

    def run(self, params={}):
        report = self.connection.any_run_api.get_report(
            params.get(Input.TASK, False)
        )
        return {
            Output.REPORTS: report.get("data", {})
        }
