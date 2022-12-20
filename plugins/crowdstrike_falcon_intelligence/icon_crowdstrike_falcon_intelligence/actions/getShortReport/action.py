import insightconnect_plugin_runtime
from .schema import GetShortReportInput, GetShortReportOutput, Input, Output, Component

# Custom imports below

from icon_crowdstrike_falcon_intelligence.util.constants import TextCase
from icon_crowdstrike_falcon_intelligence.util.helpers import convert_dict_keys_case


class GetShortReport(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="getShortReport",
            description=Component.DESCRIPTION,
            input=GetShortReportInput(),
            output=GetShortReportOutput(),
        )

    def run(self, params: dict = None):
        return {
            Output.REPORTS: convert_dict_keys_case(
                self.connection.api_client.get_short_report(params.get(Input.IDS)), TextCase.CAMEL_CASE
            )
        }
