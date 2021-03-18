import insightconnect_plugin_runtime
from .schema import EnableAgentInput, EnableAgentOutput, Input, Output, Component
# Custom imports below


class EnableAgent(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="enable_agent",
            description=Component.DESCRIPTION,
            input=EnableAgentInput(),
            output=EnableAgentOutput(),
        )

    def run(self, params={}):
        agent = params.get(Input.AGENT)
        user_filter = params.get(Input.FILTER, {})
        reboot = params.get(Input.REBOOT)
        if agent:
            user_filter["uuid"] = self.connection.client.get_agent_uuid(agent)

        return {Output.AFFECTED: self.connection.enable_agent(reboot, user_filter).get("data", {}).get("affected", 0)}
