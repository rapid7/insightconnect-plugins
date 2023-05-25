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
            return {
                Output.ID: response.response.dict().get("id", ""),
                Output.TYPE: response.response.dict().get("type", ""),
                Output.DIGEST: response.response.dict().get("digest", {}),
                Output.ANALYSIS_COMPLETION_DATE_TIME: response.response.dict().get(
                    "analysis_completion_date_time", ""
                ),
                Output.ARGUMENTS: response.response.dict().get("arguments", ""),
                Output.DETECTION_NAMES: response.response.dict().get(
                    "detection_names", []
                ),
                Output.RISK_LEVEL: response.response.dict().get("risk_level", ""),
                Output.THREAT_TYPES: response.response.dict().get("threat_types", []),
                Output.TRUE_FILE_TYPE: response.response.dict().get(
                    "true_file_type", ""
                ),
            }
