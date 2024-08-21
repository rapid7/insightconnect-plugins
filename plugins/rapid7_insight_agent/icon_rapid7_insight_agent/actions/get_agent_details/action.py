import insightconnect_plugin_runtime
from .schema import GetAgentDetailsInput, GetAgentDetailsOutput, Input, Output, Component

from insightconnect_plugin_runtime.helper import clean


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
        next_cursor = params.get(Input.NEXT_CURSOR)
        agent, next_cursor = self.connection.api.get_agent(agent_input, next_cursor)
        # Need to rename agent due to bug in yaml typing
        if agent:
            agent["agent_info"] = agent.pop("agent")

        return clean({Output.AGENT: agent, Output.NEXT_CURSOR: next_cursor})
