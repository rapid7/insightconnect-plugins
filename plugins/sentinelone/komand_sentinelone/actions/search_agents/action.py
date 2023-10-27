import insightconnect_plugin_runtime
from .schema import SearchAgentsInput, SearchAgentsOutput, Input, Output, Component

# Custom imports below


class SearchAgents(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_agents",
            description=Component.DESCRIPTION,
            input=SearchAgentsInput(),
            output=SearchAgentsOutput(),
        )

    def run(self, params={}):
        agent_active = params.get(Input.AGENTACTIVE)
        return {
            Output.AGENTS: self.connection.client.search_agents(
                params.get(Input.AGENT),
                agent_active=None if not agent_active else agent_active == "True",
                api_version="2.1",
                operational_state=params.get(Input.OPERATIONALSTATE, None),
            )
        }
