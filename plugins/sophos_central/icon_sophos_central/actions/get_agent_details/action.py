import insightconnect_plugin_runtime
from .schema import GetAgentDetailsInput, GetAgentDetailsOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_sophos_central.util.helpers import matches_entity


class GetAgentDetails(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_agent_details",
            description=Component.DESCRIPTION,
            input=GetAgentDetailsInput(),
            output=GetAgentDetailsOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        agent = params.get(Input.AGENT)
        # END INPUT BINDING - DO NOT REMOVE

        searched_agents = [
            endpoint for endpoint in self.connection.client.get_all_endpoints() if matches_entity(agent, endpoint)
        ]

        if len(searched_agents) > 1:
            self.logger.info(
                f"Multiple agents found that matched the query: {searched_agents}." f"We will act upon the first match"
            )

        if len(searched_agents) > 0:
            return {Output.AGENT: searched_agents[0]}

        raise PluginException(preset=PluginException.Preset.NOT_FOUND)
