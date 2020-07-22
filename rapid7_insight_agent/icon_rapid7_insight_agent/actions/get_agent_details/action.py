import insightconnect_plugin_runtime
from .schema import GetAgentDetailsInput, GetAgentDetailsOutput, Input, Output, Component
# Custom imports below
import icon_rapid7_insight_agent.util.get_agent as get_agent
import icon_rapid7_insight_agent.util.agent_typer as agent_typer

class GetAgentDetails(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_agent_details',
                description=Component.DESCRIPTION,
                input=GetAgentDetailsInput(),
                output=GetAgentDetailsOutput())

    def run(self, params={}):
        agent_input = params.get(Input.AGENT)
        agent_type = agent_typer.get_agent_type(agent_input)
        agents = get_agent.get_all_agents(self.connection, self.logger)
        agent = get_agent.find_agent_in_agents(agents, agent_input, agent_type, self.logger)
        return {Output.AGENT: agent}


