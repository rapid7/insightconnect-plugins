import insightconnect_plugin_runtime
from .schema import CloseCaseInput, CloseCaseOutput, Component, Input, Output

# Custom imports below


class CloseCase(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="close_case",
            description=Component.DESCRIPTION,
            input=CloseCaseInput(),
            output=CloseCaseOutput(),
        )

    def run(self, params={}):

        case_id = params.get(Input.ID)
        force = params.get(Input.FORCE)

        response = self.connection.client.close_case(case_id=case_id, force=force)

        return {Output.SUCCESS: response}
