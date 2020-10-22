import insightconnect_plugin_runtime
from .schema import SearchThreatAgentsInput, SearchThreatAgentsOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
# Custom imports below


class SearchThreatAgents(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_threat_agents',
                description=Component.DESCRIPTION,
                input=SearchThreatAgentsInput(),
                output=SearchThreatAgentsOutput())

    def run(self, params={}):
        threat_identifier = params.get(Input.THREAT_IDENTIFIER)
        matching_threats = self.connection.client.search_threats([threat_identifier])
        if len(matching_threats) > 1:
            self.logger.info(
                f"Multiple threats found that matched the query: {threat_identifier}. "
                "We will only act upon the first match"
                )

        agents = self.get_all_threat_agents(matching_threats[0].get('sha256'))

        if len(agents) == 0:
            raise PluginException(
                cause="No agents found.",
                assistance=f"No agents related to: {threat_identifier} found."
            )

        return {
            Output.AGENTS: agents
        }

    def get_all_threat_agents(self, sha256: str) -> list:
        i = 1
        total_pages = self.connection.client.get_threat_devices(sha256, i, "200").get('total_pages')
        agents = []
        while i <= total_pages:
            response = self.connection.client.get_threat_devices(sha256, i, "200")
            device_list = response.get('page_items')
            for device in device_list:
                agents.append(device)
            i += 1

        return agents
