import insightconnect_plugin_runtime
from .schema import GetAgentDetailsInput, GetAgentDetailsOutput, Input, Output, Component

# Custom imports below


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
            case_sensitive=params.get(Input.CASE_SENSITIVE),
            api_version="2.1",
            operational_state=params.get(Input.OPERATIONAL_STATE, None),
        )

        if len(output) > 1:
            self.logger.info(
                f"Multiple agents found that matched the query: {agent}. We will only act upon the first match"
            )

        if len(output) == 0:
            return {Output.AGENT: {}}

        return {Output.AGENT: output[0]}
