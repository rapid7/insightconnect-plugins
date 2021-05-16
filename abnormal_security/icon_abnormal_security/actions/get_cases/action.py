import insightconnect_plugin_runtime
from .schema import GetCasesInput, GetCasesOutput, Input, Output, Component

# Custom imports below


class GetCases(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_cases", description=Component.DESCRIPTION, input=GetCasesInput(), output=GetCasesOutput()
        )

    def run(self, params={}):
        return {
            Output.CASES: self.connection.api.get_cases(
                from_date=params.get(Input.FROM_DATE, None), to_date=params.get(Input.TO_DATE, None)
            )
        }
