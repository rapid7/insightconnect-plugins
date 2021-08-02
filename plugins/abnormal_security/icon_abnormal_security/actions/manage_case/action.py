import insightconnect_plugin_runtime
from .schema import ManageCaseInput, ManageCaseOutput, Input, Output, Component

# Custom imports below
from icon_abnormal_security.util.util import AvailableInputs


class ManageCase(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="manage_case", description=Component.DESCRIPTION, input=ManageCaseInput(), output=ManageCaseOutput()
        )

    def run(self, params={}):
        return {
            Output.RESPONSE: self.connection.api.manage_case(
                params.get(Input.CASE_ID), AvailableInputs.ManageCase.get(params.get(Input.ACTION))
            )
        }
