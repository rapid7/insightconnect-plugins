import insightconnect_plugin_runtime

from icon_crowdstrike_falcon_intelligence.util.constants import TextCase
from icon_crowdstrike_falcon_intelligence.util.helpers import convert_dict_keys_case
from .schema import CheckAnalysisStatusInput, CheckAnalysisStatusOutput, Input, Output, Component

# Custom imports below


class CheckAnalysisStatus(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="checkAnalysisStatus",
            description=Component.DESCRIPTION,
            input=CheckAnalysisStatusInput(),
            output=CheckAnalysisStatusOutput(),
        )

    def run(self, params: dict = None):
        return {
            Output.SUBMISSIONS: convert_dict_keys_case(
                self.connection.api_client.check_analysis_status(params.get(Input.IDS)), TextCase.CAMEL_CASE
            )
        }
