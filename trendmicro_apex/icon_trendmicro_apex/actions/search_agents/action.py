import komand
from .schema import SearchAgentsInput, SearchAgentsOutput, Input, Output, Component
# Custom imports below
import re
import urllib.parse


class SearchAgents(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='search_agents',
            description=Component.DESCRIPTION,
            input=SearchAgentsInput(),
            output=SearchAgentsOutput())

    def run(self, params={}):
        agent_ids = params.get(Input.AGENT_IDS)
        query_params = {}
        quoted_param = ""

        entity_pattern = re.compile(r'^[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{8}$')
        ip_address_pattern = re.compile(r'^(?:\d{1,3}\.){3}\d{1,3}$')
        mac_address_pattern = re.compile(r'\d\d([-:]\d\d){5}')
        if agent_ids:
            for agent_id in agent_ids:
                if re.match(mac_address_pattern, agent_id):
                    query_params["mac_address"] = agent_id
                elif re.match(ip_address_pattern, agent_id):
                    query_params["ip_address"] = agent_id
                elif re.match(entity_pattern, agent_id):
                    query_params["entity_id"] = agent_id
                else:
                    query_params["host_name"] = agent_id

            quoted_param = urllib.parse.quote("&".join([k + "=" + v for k, v in query_params.items()]))
            if quoted_param:
                quoted_param = "?" + quoted_param

        agents = self.connection.api.execute(
            "get",
            "/WebApp/API/AgentResource/ProductAgents" + quoted_param,
            ""
        )

        if agents.get("result_code", 0) == 1:
            f = agents.get("result_content")
            self.logger.info(f"result_content: {f}")
            return {
                Output.SEARCH_AGENT_RESPONSE: agents.get("result_content")
            }

        return {
            Output.SEARCH_AGENT_RESPONSE: []
        }
