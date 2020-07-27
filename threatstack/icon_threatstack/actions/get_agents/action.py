import insightconnect_plugin_runtime
from .schema import GetAgentsInput, GetAgentsOutput, Input, Output
# Custom imports below
from insightconnect_plugin_runtime.helper import clean
from threatstack.errors import ThreatStackAPIError, ThreatStackClientError, APIRateLimitError
from insightconnect_plugin_runtime.exceptions import PluginException


class GetAgents(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_agents',
                description='Get agent data',
                input=GetAgentsInput(),
                output=GetAgentsOutput())

    def run(self, params={}):
        start, end = params.get(Input.START), params.get(Input.END)
        try:
            agents = self.connection.client.agents.list(start=start,
                                                        end=end)
        except (ThreatStackAPIError, ThreatStackClientError, APIRateLimitError) as e:
            raise PluginException(cause="An error occurred!",
                                  assistance=e)

        # Consume the generator
        agents = [clean(agent) for agent in agents]

        return {Output.AGENTS: agents, Output.COUNT: len(agents)}
