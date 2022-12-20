import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_crowdstrike_falcon_intelligence.util.constants import TextCase
from icon_crowdstrike_falcon_intelligence.util.helpers import convert_dict_keys_case, split_utc_date_time
from .schema import SubmitAnalysisInput, SubmitAnalysisOutput, Input, Output, Component


# Custom imports below


class SubmitAnalysis(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submitAnalysis",
            description=Component.DESCRIPTION,
            input=SubmitAnalysisInput(),
            output=SubmitAnalysisOutput(),
        )

    def run(self, params: dict = None):
        analysis_parameters = convert_dict_keys_case(params, TextCase.SNAKE_CASE)
        file_sha256 = params.get(Input.SHA256)
        file_url = params.get(Input.URL)
        analysis_parameters["system_date"], analysis_parameters["system_time"] = split_utc_date_time(
            analysis_parameters.pop("system_date_time")
        )
        if not any([file_url, file_sha256]):
            raise PluginException(
                cause="Neither sha256 nor the url were provided",
                assistance="Please provide sha256 or url parameter and try again. If the issue persists, please contact support.",
            )
        if all([file_url, file_sha256]):
            raise PluginException(
                cause="Sha256 and URL parameters used together",
                assistance="Please provide sha256 or URL parameter (not both) and try again. If the issue persists, please contact support.",
            )
        submission = convert_dict_keys_case(
            self.connection.api_client.submit_analysis(analysis_parameters), TextCase.CAMEL_CASE
        )
        submission.get("sandbox", [{}])[0].pop("documentPassword", None)
        return {Output.SUBMISSION: submission}
