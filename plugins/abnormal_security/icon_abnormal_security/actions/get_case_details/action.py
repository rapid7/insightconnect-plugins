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

        # Solution to convert Case ID to string if it gets returned as an integer
        case_id = params.get(Input.CASE_ID, "")

        response = self.connection.api.get_case_details(case_id)
        if isinstance(response.get("caseId"), int):
            response["caseId"] = str(response.get("caseId"))
        return {Output.CASE_DETAILS: response}
