import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import GetJobReportInput, GetJobReportOutput, Input, Output, Component

# Custom imports below


class GetJobReport(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_job_report",
            description=Component.DESCRIPTION,
            input=GetJobReportInput(),
            output=GetJobReportOutput(),
        )

    def run(self, params={}):
        job_id = params.get(Input.JOB_ID)
        self.logger.info(f"Getting report for job {job_id}")
        try:
            return {Output.REPORT: self.connection.API.get_job_report(job_id)}
        except Exception as error:
            raise PluginException(cause="Failed to get job report.", assistance=f"{error}")
