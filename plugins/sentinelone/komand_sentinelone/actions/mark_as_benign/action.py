import insightconnect_plugin_runtime
from .schema import MarkAsBenignInput, MarkAsBenignOutput, Input, Output, Component

# Custom imports below


class MarkAsBenign(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="mark_as_benign",
            description=Component.DESCRIPTION,
            input=MarkAsBenignInput(),
            output=MarkAsBenignOutput(),
        )

    def run(self, params={}):
        response = self.connection.client.mark_as_benign(
            params.get(Input.THREATID),
            params.get(Input.WHITENINGOPTION) or None,
            params.get(Input.TARGETSCOPE),
        )
        return {Output.AFFECTED: response.get("data", {}).get("affected", 0)}
