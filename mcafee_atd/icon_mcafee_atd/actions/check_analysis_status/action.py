import insightconnect_plugin_runtime
from .schema import CheckAnalysisStatusInput, CheckAnalysisStatusOutput, Input, Output, Component


# Custom imports below


class CheckAnalysisStatus(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='check_analysis_status',
            description=Component.DESCRIPTION,
            input=CheckAnalysisStatusInput(),
            output=CheckAnalysisStatusOutput())

    def run(self, params={}):
        status = self.connection.mcafee_atd_api.check_analysis_status(
            params.get(Input.ANALYSIS_ID),
            params.get(Input.TYPE, "task")
        )
        success = status.get("success", False)

        if "task" == params.get(Input.TYPE, "task"):
            return {
                Output.SUCCESS: success,
                Output.RESULTS: status.get("results")
            }

        del status["success"]
        return {
            Output.SUCCESS: success,
            Output.JOB_RESULTS: status
        }
