import insightconnect_plugin_runtime
from .schema import GetAgentDetailsInput, GetAgentDetailsOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.helper import clean
from icon_symantec_endpoint_security.util.api import APIException, Agent
from insightconnect_plugin_runtime.exceptions import PluginException
from typing import Optional

import re


class GetAgentDetails(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_agent_details',
                description=Component.DESCRIPTION,
                input=GetAgentDetailsInput(),
                output=GetAgentDetailsOutput())

    def run(self, params={}):
        query = params.get(Input.AGENT)
        is_mac = self._is_search_mac_address(query=query)

        try:
            if is_mac:
                match: Optional[Agent] = self.connection.api_client.get_computer(mac_address=query)
            else:  # hostname
                match: Optional[Agent] = self.connection.api_client.get_computer(computer_name=query)
            return {Output.AGENT: clean(match)}

        except APIException as e:
            raise PluginException(cause="An error occurred while attempting to get agent details!",
                                  assistance=e.message)

    @staticmethod
    def _is_search_mac_address(query: str) -> bool:
        """
        Determines whether or not a search query given is a MAC address or computer hostname
        :param query: Query string input by the user
        :return: Boolean indicating if the query given was a MAC address (true)
        """
        r = r"([a-fA-F0-9]{2}[-:]){5}[a-zA-Z0-9]{2}"
        matches = re.match(r, query)

        if matches:
            return True

        return False
