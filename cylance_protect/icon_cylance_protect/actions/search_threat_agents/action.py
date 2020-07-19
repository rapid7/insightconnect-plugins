import insightconnect_plugin_runtime
from .schema import SearchThreatAgentsInput, SearchThreatAgentsOutput, Input, Output, Component
# Custom imports below


class SearchThreatAgents(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_threat_agents',
                description=Component.DESCRIPTION,
                input=SearchThreatAgentsInput(),
                output=SearchThreatAgentsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
