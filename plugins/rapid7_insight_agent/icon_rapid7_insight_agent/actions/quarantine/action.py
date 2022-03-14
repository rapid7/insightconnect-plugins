import insightconnect_plugin_runtime
from .schema import QuarantineInput, QuarantineOutput, Input, Output, Component

# Custom imports below


class Quarantine(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="quarantine",
            description=Component.DESCRIPTION,
            input=QuarantineInput(),
            output=QuarantineOutput(),
        )

    def run(self, params={}):
        agent_id = params.get(Input.AGENT_ID)
        advertisement_period = params.get(Input.INTERVAL)
        quarantine_state = params.get(Input.QUARANTINE_STATE)

        agent_id_stripped = agent_id.replace("-", "")

        if quarantine_state:
            success = self.connection.api.quarantine(advertisement_period, agent_id_stripped)
        else:
            success = self.connection.api.unquarantine(agent_id_stripped)

        return {Output.SUCCESS: success}
