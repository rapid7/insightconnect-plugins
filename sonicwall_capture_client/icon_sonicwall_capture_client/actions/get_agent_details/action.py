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
        all_endpoints = self.connection.client.get_endpoints_list()
        agent = params.get(Input.AGENT)
        searched_agents = []

        for e in all_endpoints:
            if self._is_agent_found(agent, e):
                searched_agents.append(e)

        if len(searched_agents) > 1:
            self.logger.info(
                f"Multiple agents found that matched the query: {searched_agents}."
                f"We will act upon the first match."
            )

        if len(searched_agents) > 0:
            device_id = searched_agents[0].get("deviceId")
            install_token = searched_agents[0].get("installToken")

            return {
                Output.AGENT: insightconnect_plugin_runtime.helper.clean(
                    self.connection.client.get_endpoint(device_id, install_token)
                )
            }

        raise PluginException(cause="Unable to return information about provided agent.",
                              assistance="Please provide an existed agent information.")

    @staticmethod
    def _is_agent_found(agent, e):
        return e.get("deviceId") == agent \
               or e.get("name") == agent \
               or e.get("domain") == agent \
               or e.get("localIp") == agent \
               or e.get("ip") == agent \
               or GetAgentDetails._is_mac(agent, e)

    @staticmethod
    def _is_mac(agent, e):
        if e.get("macAddress") == agent:
            return True

        normalize_mac = e.get("macAddress").lower().replace("-", "").replace(":", "")
        normalize_agent = agent.lower().replace("-", "").replace(":", "")
        return normalize_mac == normalize_agent
