import insightconnect_plugin_runtime
from .schema import GetAgentDetailsInput, GetAgentDetailsOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.helper import return_non_empty


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
        agent = params.get(Input.AGENT, "")
        # END INPUT BINDING - DO NOT REMOVE

        device = self.connection.get_agent(agent)
        return {Output.AGENT: return_non_empty(device)}
