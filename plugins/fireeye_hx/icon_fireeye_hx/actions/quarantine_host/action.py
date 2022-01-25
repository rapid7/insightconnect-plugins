import insightconnect_plugin_runtime
from .schema import QuarantineHostInput, QuarantineHostOutput, Input, Output, Component

# Custom imports below


class QuarantineHost(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="quarantine_host",
            description=Component.DESCRIPTION,
            input=QuarantineHostInput(),
            output=QuarantineHostOutput(),
        )

    def run(self, params={}):
        return {Output.SUCCESS: self.connection.api.quarantine_host(params.get(Input.AGENT_ID))}
