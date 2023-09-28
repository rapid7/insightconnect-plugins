import insightconnect_plugin_runtime
from .schema import MitigateThreatInput, MitigateThreatOutput, Input, Output

# Custom imports below


class MitigateThreat(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="mitigate_threat",
            description="Apply a mitigation action to a threat",
            input=MitigateThreatInput(),
            output=MitigateThreatOutput(),
        )

    def run(self, params={}):
        response = self.connection.client.mitigate_threat(params.get(Input.THREATID), params.get(Input.ACTION))
        return {Output.AFFECTED: response.get("data", {}).get("affected", 0)}
