import insightconnect_plugin_runtime
from .schema import (
    GetAgentDetailsInput,
    GetAgentDetailsOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


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
        output = self.connection.client.search_agents(
            agent,
            operational_state=params.get(Input.OPERATIONALSTATE, None),
        )

        if len(output) > 1:
            raise PluginException(
                cause="Multiple agents found.",
                assistance="Please provide a unique agent identifier so the action can be performed on the intended "
                "agent.",
            )

        return {Output.AGENT: {} if len(output) == 0 else output[0]}
