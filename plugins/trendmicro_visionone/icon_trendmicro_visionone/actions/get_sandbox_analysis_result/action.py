import insightconnect_plugin_runtime
from .schema import (
    GetSandboxAnalysisResultInput,
    GetSandboxAnalysisResultOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class GetSandboxAnalysisResult(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_sandbox_analysis_result",
            description=Component.DESCRIPTION,
            input=GetSandboxAnalysisResultInput(),
            output=GetSandboxAnalysisResultOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        report_id = params.get(Input.REPORT_ID)
        poll = params.get(Input.POLL)
        poll_time_sec = params.get(Input.POLL_TIME_SEC)
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.get_sandbox_analysis_result(
            submit_id=report_id,
            poll=poll,
            poll_time_sec=poll_time_sec,
        )
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while getting the sandbox analysis result.",
                assistance="Please check the report ID and try again.",
                data=response,
            )
        else:
            self.logger.info("Returning Results...")
            return response.response.dict()
