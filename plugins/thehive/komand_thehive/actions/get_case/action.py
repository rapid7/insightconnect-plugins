import insightconnect_plugin_runtime
from .schema import GetCaseInput, GetCaseOutput, Input, Output, Component

# Custom imports below


class GetCase(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_case",
            description=Component.DESCRIPTION,
            input=GetCaseInput(),
            output=GetCaseOutput(),
        )

    def run(self, params={}):

        case_id = params.get(Input.ID)

        result = self.connection.client.get_case(case_id)

        return {Output.CASE: result}
