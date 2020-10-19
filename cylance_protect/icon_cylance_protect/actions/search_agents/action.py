import insightconnect_plugin_runtime
from .schema import SearchAgentsInput, SearchAgentsOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
# Custom imports below
# Custom imports below
from icon_cylance_protect.util.find_helpers import find_in_whitelist, find_agent_by_ip
import validators


class SearchAgents(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_agents',
                description=Component.DESCRIPTION,
                input=SearchAgentsInput(),
                output=SearchAgentsOutput())

    def run(self, params={}):
        # If IPv4, attempt to find its ID first
        agent = params.get(Input.AGENT)
        if validators.ipv4(agent):
            agent = find_agent_by_ip(self.connection, agent)

        return {
            Output.AGENTS: self.connection.client.search_agents_all(agent)
        }
