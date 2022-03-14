import insightconnect_plugin_runtime
from .schema import GetAgentDetailsInput, GetAgentDetailsOutput, Input, Output, Component


# Custom imports below


class GetAgentDetails(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_agent_details",
            description=Component.DESCRIPTION,
            input=GetAgentDetailsInput(),
            output=GetAgentDetailsOutput(),
        )

    def run(self, params={}):
        agent_input = params.get(Input.AGENT)
        agent = self.connection.api.get_agent(agent_input)
        # Need to rename agent due to bug in yaml typing
        agent["agent_info"] = agent.pop("agent")

        return {Output.AGENT: agent}
