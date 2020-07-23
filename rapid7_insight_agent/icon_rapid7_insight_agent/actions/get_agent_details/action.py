import insightconnect_plugin_runtime
from .schema import GetAgentDetailsInput, GetAgentDetailsOutput, Input, Output, Component
# Custom imports below
from icon_rapid7_insight_agent.util.graphql_api.api_exception import APIException
from insightconnect_plugin_runtime.exceptions import PluginException

class GetAgentDetails(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_agent_details',
                description=Component.DESCRIPTION,
                input=GetAgentDetailsInput(),
                output=GetAgentDetailsOutput())

    def run(self, params={}):
        agent_input = params.get(Input.AGENT)
        try:
            agent = self.connection.api.get_agent(agent_input)
        except APIException as e:
            raise PluginException(cause = e.cause,
                                  assistance = e.assistance,
                                  data = e.data)

        return {Output.AGENT: agent}


