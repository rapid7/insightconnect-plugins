import insightconnect_plugin_runtime
from .schema import GetReportInput, GetReportOutput, Input, Output, Component

# Custom imports below


class GetReport(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_report",
            description=Component.DESCRIPTION,
            input=GetReportInput(),
            output=GetReportOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        task = params.get(Input.TASK, False)
        # END INPUT BINDING - DO NOT REMOVE

        report = self.connection.any_run_api.get_report(task)
        return {Output.REPORTS: insightconnect_plugin_runtime.helper.clean(report.get("data", {}))}
