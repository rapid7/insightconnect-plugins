import insightconnect_plugin_runtime
from .schema import GetCasesInput, GetCasesOutput, Input, Output, Component

# Custom imports below


class GetCases(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_cases", description=Component.DESCRIPTION, input=GetCasesInput(), output=GetCasesOutput()
        )

    def run(self, params={}):
        response = self.connection.api.get_cases(
            from_date=params.get(Input.FROM_DATE),
            to_date=params.get(Input.TO_DATE),
            filter_key=params.get(Input.FILTER_KEY, "lastModifiedTime"),
        )
        # Solution to convert Case ID to string if it gets returned as an integer
        for case in response:
            if isinstance(case.get("caseId"), int):
                case["caseId"] = str(case["caseId"])
        return {Output.CASES: response}
