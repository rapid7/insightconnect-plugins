import insightconnect_plugin_runtime
from .schema import SearchAgentsInput, SearchAgentsOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
# Custom imports below


class SearchAgents(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_agents',
                description=Component.DESCRIPTION,
                input=SearchAgentsInput(),
                output=SearchAgentsOutput())

    def run(self, params={}):
        return {
            Output.AGENTS: self.search_agents(params.get(Input.AGENT))
        }
