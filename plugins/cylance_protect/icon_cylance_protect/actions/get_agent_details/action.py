import insightconnect_plugin_runtime
from .schema import GetAgentDetailsInput, GetAgentDetailsOutput, Input, Output, Component

# Custom imports below

import validators
from icon_cylance_protect.util.find_helpers import find_agent_by_ip


class GetAgentDetails(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_agent_details",
            description=Component.DESCRIPTION,
            input=GetAgentDetailsInput(),
            output=GetAgentDetailsOutput(),
        )

    def run(self, params={}):

        agent = params.get(Input.AGENT)

        if validators.ipv4(agent):
            agent = find_agent_by_ip(self.connection, agent)

        device = self.connection.client.get_agent_details(agent)
        return {Output.AGENT: device}
