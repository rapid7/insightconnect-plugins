import insightconnect_plugin_runtime
from .schema import RemoveExemptionInput, RemoveExemptionOutput, Input, Output, Component

# Custom imports below


class RemoveExemption(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove_exemption",
            description=Component.DESCRIPTION,
            input=RemoveExemptionInput(),
            output=RemoveExemptionOutput(),
        )

    def run(self, params={}):
        json_data = {"exemption_ids": params.get(Input.EXEMPTIONIDS)}
        return {Output.SUCCESS: self.connection.api.remove_exemption(json_data)}
