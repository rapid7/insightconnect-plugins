import insightconnect_plugin_runtime
from .schema import MarkAsThreatInput, MarkAsThreatOutput, Input, Output, Component

# Custom imports below


class MarkAsThreat(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="mark_as_threat",
            description=Component.DESCRIPTION,
            input=MarkAsThreatInput(),
            output=MarkAsThreatOutput(),
        )

    def run(self, params={}):
        response = self.connection.client.mark_as_threat(
            params.get(Input.THREATID),
            params.get(Input.WHITENINGOPTION) or None,
            params.get(Input.TARGETSCOPE),
        )
        return {Output.AFFECTED: response.get("data", {}).get("affected", 0)}
