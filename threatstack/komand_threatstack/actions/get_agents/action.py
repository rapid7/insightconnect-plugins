import komand
from .schema import GetAgentsInput, GetAgentsOutput, Input, Output
# Custom imports below


class GetAgents(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_agents',
                description='Get agent data',
                input=GetAgentsInput(),
                output=GetAgentsOutput())

    def run(self, params={}):
        start, end = params.get(Input.START), params.get(Input.END)
        agents = self.connection.client.agents.list(start=start,
                                                    end=end)

        # Consume the generator
        agents = [agent for agent in agents]

        return {Output.AGENTS: agents, Output.COUNT: len(agents)}
