import insightconnect_plugin_runtime
from .schema import GetAgentDetailsInput, GetAgentDetailsOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import requests


class GetAgentDetails(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_agent_details',
                description=Component.DESCRIPTION,
                input=GetAgentDetailsInput(),
                output=GetAgentDetailsOutput())

    def run(self, params={}):

        agents = []

        headers = self.connection.get_headers()

        #TODO: Change limit to 10000
        payload = {
            "query": "query($orgId: String!) {organization(id: $orgId) { assets(first: 1) { pageInfo { hasNextPage endCursor } edges { node { host { id vendor version description hostNames { name } primaryAddress { ip mac } uniqueIdentity { source id } attributes { key value } } id agent { id } } } } } } ",
            "variables": {
                "orgId": "3af18a2c-432f-4bce-af67-93711c509704"
            }
        }

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

        while has_next_page:
            next_cursor = results_object.get("data").get("organization").get("assets").get("pageInfo").get("endCursor")
            payload = {
                "query": "query($orgId: String! $nextCursor: String!) {organization(id: $orgId) { assets(first: 1 after: $nextCursor) { pageInfo { hasNextPage endCursor } edges { node { host { id vendor version description hostNames { name } primaryAddress { ip mac } uniqueIdentity { source id } attributes { key value } } id agent { id } } } } } } ",
                "variables": {
                    "orgId": self.connection.org_key,
                    "nextCursor": next_cursor
                }
            }
            result = requests.post(self.connection.endpoint, headers=headers, data=payload)

            results_object = result.json()
            has_next_page = results_object.get("data").get("organization").get("assets").get("pageInfo").get(
                "hasNextPage")

            agents.extend(self.get_agents_from_result_object(results_object))

        return {Output.AGENT: agents[0]}

    def get_agents_from_result_object(self, results_object):
        agent_list = []

        edges = results_object.get("data").get("organization").get("assets").get("edges")
        for edge in edges:
            agent = edge.get("node").get("host")
            agent_list.append(agent)

        return agent_list
