import insightconnect_plugin_runtime
from .schema import GetCaseDetailsInput, GetCaseDetailsOutput, Input, Output, Component

# Custom imports below


class GetCaseDetails(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_case_details",
            description=Component.DESCRIPTION,
            input=GetCaseDetailsInput(),
            output=GetCaseDetailsOutput(),
        )

    def run(self, params={}):
        return {Output.CASE_DETAILS: self.connection.api.get_case_details(params.get(Input.CASE_ID))}
