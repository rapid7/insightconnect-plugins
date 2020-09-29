import komand
from .schema import SearchAgentsInput, SearchAgentsOutput, Input, Output, Component
# Custom imports below


class SearchAgents(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='search_agents',
            description=Component.DESCRIPTION,
            input=SearchAgentsInput(),
            output=SearchAgentsOutput())

    def run(self, params={}):
        return {
            Output.AGENTS: self.connection.client.search_agents(
                params.get(Input.AGENT),
                params.get(Input.AGENT_ACTIVE, True)
            )
        }
