import insightconnect_plugin_runtime
from .schema import ManageThreatInput, ManageThreatOutput, Input, Output, Component

# Custom imports below


class ManageThreat(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="manage_threat",
            description=Component.DESCRIPTION,
            input=ManageThreatInput(),
            output=ManageThreatOutput(),
        )

    def run(self, params={}):
        return {
            Output.RESPONSE: self.connection.api.manage_threat(params.get(Input.THREAT_ID), params.get(Input.ACTION))
        }
