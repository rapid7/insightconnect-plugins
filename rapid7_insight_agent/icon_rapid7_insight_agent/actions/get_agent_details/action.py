import insightconnect_plugin_runtime
from .schema import GetAgentDetailsInput, GetAgentDetailsOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import icon_rapid7_insight_agent.util.agent_typer as agent_typer
import requests


class GetAgentDetails(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_agent_details',
                description=Component.DESCRIPTION,
                input=GetAgentDetailsInput(),
                output=GetAgentDetailsOutput())

    def run(self, params={}):
        agent_input = params.get(Input.AGENT)
        agent_type = agent_typer.get_agent_type(agent_input)
        agents = self.get_all_agents()
        agent = self.find_agent_in_agents(agents, agent_input, agent_type)
        return {Output.AGENT: agent}

    def get_all_agents(self):
        agents = []
        headers = self.connection.get_headers()
        # TODO: Change limit to 10000
        payload = {
            "query": "query($orgId: String!) {organization(id: $orgId) { assets(first: 1) { pageInfo { hasNextPage endCursor } edges { node { host { id vendor version description hostNames { name } primaryAddress { ip mac } uniqueIdentity { source id } attributes { key value } } id agent { id } } } } } } ",
            "variables": {
                "orgId": "3af18a2c-432f-4bce-af67-93711c509704"
            }
        }

        self.logger.info(f"Getting agents from: {self.connection.endpoint}")
        result = requests.post(self.connection.endpoint, headers=headers, json=payload)
        try:
            result.raise_for_status()
        except:
            raise PluginException(cause="Could not get results from Insight Agent API",
                                  assistance="Please verify your Organization ID and API Key\n",
                                  data=result.text)
        results_object = result.json()
        if results_object.get("errors"):
            raise PluginException(cause="Insight Agent API returned errors",
                                  assistance=results_object.get("errors"))
        has_next_page = results_object.get("data").get("organization").get("assets").get("pageInfo").get("hasNextPage")
        agents.extend(self.get_agents_from_result_object(results_object))
        self.logger.info(f"Initial agents received.")

        # See if we have more pages of data, if so get next page and append until we reach the end
        while has_next_page:
            has_next_page, results_object = self.get_next_page_of_agents(agents, headers, results_object)

        self.logger.info(f"Done getting all agents.")

        return agents

    def get_next_page_of_agents(self, agents, headers, results_object):
        self.logger.info(f"Getting next page of agents.")
        next_cursor = results_object.get("data").get("organization").get("assets").get("pageInfo").get("endCursor")
        payload = {
            "query": "query( $orgId:String! $nextCursor:String! ) { organization(id: $orgId) { assets( first: 1 after: $nextCursor ) { pageInfo { hasNextPage endCursor } edges { node { host { id vendor version description hostNames { name } primaryAddress { ip mac } uniqueIdentity { source id } attributes { key value } } id agent { id } } } } } }",
            "variables": {
                "orgId": self.connection.org_key,
                "nextCursor": next_cursor
            }
        }
        result = requests.post(self.connection.endpoint, headers=headers, json=payload)
        results_object = result.json()
        has_next_page = results_object.get("data").get("organization").get("assets").get("pageInfo").get(
            "hasNextPage")
        next_agents = self.get_agents_from_result_object(results_object)
        agents.extend(next_agents)
        return has_next_page, results_object

    def find_agent_in_agents(self, agents, agent_input, agent_type):
        """
        {'id': '15eec979a15f75ad70567d58ad8a0aef', 'vendor': 'Microsoft', 'version': 'SP1', 'description': 'Microsoft Windows 7 Professional SP1', 'hostNames': [{'name': 'joey-w7-vagrant-pc'}], 'primaryAddress': {'ip': '10.0.2.15', 'mac': '08-00-27-33-9F-CE'}, 'uniqueIdentity': [{'source': 'Endpoint Agent', 'id': '15eec979a15f75ad70567d58ad8a0aef'}, {'source': 'CSPRODUCT', 'id': '030B19C0-F12D-6643-B86E-FA7C08A4A838'}], 'attributes': [{'key': 'cpuinfo', 'value': 'Intel(R) Core(TM) i7-6920HQ CPU @ 2.90GHz'}, {'key': 'timezone', 'value': 'GMT-7'}, {'key': 'release', 'value': '7'}, {'key': 'proxies', 'value': '{}'}]}
        """
        self.logger.info(f"Searching for: {agent_input}")
        self.logger.info(f"Search type: {agent_type}")
        for agent in agents:
            if agent_type == agent_typer.IP_ADDRESS:
                if agent_input == agent.get("primaryAddress").get("ip"):
                    return agent
            elif agent_type == agent_typer.HOSTNAME:
                # In this case, we have an alpha/numeric value. This could be the ID or the Hostname. Need to check both
                if agent_input == agent.get("id"):
                    return agent
                for host_name in agent.get("hostNames"):
                    if agent_input == host_name.get("name"):
                        return agent
            elif agent_type == agent_typer.MAC_ADDRESS:
                stripped_input_mac = agent_input.replace("-","").replace(":","")
                stripped_target_mac = agent.get("primaryAddress").get("mac").replace("-","").replace(":","")
                if stripped_input_mac == stripped_target_mac:
                    return agent
            else:
                raise PluginException(cause="Could not determine agent type",
                                      assistance=f"Agent {agent_input} was not a Mac, IP, or Hostname.")

        raise PluginException(cause=f"Could not find agent matching {agent_input} of type {agent_type}",
                              assistance=f"Check the agent input value and try again.")

    def get_agents_from_result_object(self, results_object):
        agent_list = []

        edges = results_object.get("data").get("organization").get("assets").get("edges")
        for edge in edges:
            agent = edge.get("node").get("host")
            agent_list.append(agent)

        return agent_list
