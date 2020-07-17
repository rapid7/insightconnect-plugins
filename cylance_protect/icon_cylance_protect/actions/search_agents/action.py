import insightconnect_plugin_runtime
from .schema import SearchAgentsInput, SearchAgentsOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
# Custom imports below
import validators
import re


class SearchAgents(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_agents',
                description=Component.DESCRIPTION,
                input=SearchAgentsInput(),
                output=SearchAgentsOutput())

    def run(self, params={}):
        agent = params.get(Input.AGENT)

        return {
            Output.AGENTS: self.find_agents(agent.lower(), self.identify_input_type(agent))
        }

    @staticmethod
    def identify_input_type(agent: str) -> str:
        if re.match('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', agent):
            return 'ip_address'
        elif re.match('[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$', agent.lower()):
            return 'mac_address'
        elif re.match('^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$', agent.lower()):
            return 'id'
        else:
            return 'hostname'

    def find_agents(self, agent: str, identifier_type: str) -> list:
        i = 1
        total_pages = self.connection.client.get_agents(i, '20').get('total_pages')
        agents = []

        while i <= total_pages:
            response = self.connection.client.get_agents(i, "20")
            device_list = response.get('page_items')
            if identifier_type == 'ip_address':
                for device in device_list:
                    for ip in device.get('ip_addresses'):
                        if agent == ip:
                            agents.append(device)
            if identifier_type == 'mac_address':
                for device in device_list:
                    for mac in device.get('mac_addresses'):
                        if agent.replace(':', '-').upper() == mac:
                            agents.append(device)
            if identifier_type == 'id':
                for device in device_list:
                        if agent.lower() == device.get('id'):
                            agents.append(device)
            if identifier_type == 'hostname':
                for device in device_list:
                        if agent.upper() == device.get('name').upper():
                            agents.append(device)

            i += 1

        if agents:
            return agents

        raise PluginException(
            cause="Agent not found.",
            assistance=f"Unable to find agents using identifier provided: {agent}."
        )
