import insightconnect_plugin_runtime
from .schema import GetAgentDetailsInput, GetAgentDetailsOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class GetAgentDetails(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_agent_details',
            description=Component.DESCRIPTION,
            input=GetAgentDetailsInput(),
            output=GetAgentDetailsOutput())

    def run(self, params={}):
        page_key = None
        agent = params.get(Input.AGENT)
        all_endpoints = []

        for index in range(9999):
            endpoints = self.connection.client.get_endpoints(page_key=page_key)
            page_key = endpoints.get("pages", {}).get("nextKey", None)
            all_endpoints.extend(endpoints.get("items", []))

            if page_key is None or index > endpoints.get("pages", {}).get("total", 0):
                break

        searched_agents = []
        for e in all_endpoints:
            if self._is_agent_found(agent, e):
                searched_agents.append(e)

        if len(searched_agents) > 1:
            self.logger.info(
                f"Multiple agents found that matched the query: {searched_agents}."
                f"We will act upon the first match"
            )

        if len(searched_agents) > 0:
            return {
                Output.AGENT: searched_agents[0]
            }

        raise PluginException(preset=PluginException.Preset.NOT_FOUND)

    @staticmethod
    def _is_agent_found(agent, e):
        return e.get("hostname") == agent \
               or e.get("id") == agent \
               or agent in e.get("ipv4Addresses") \
               or agent in e.get("macAddresses") \
               or agent in e.get("ipv6Addresses")
