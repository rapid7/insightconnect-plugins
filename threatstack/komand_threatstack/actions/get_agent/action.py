import insightconnect_plugin_runtime
from .schema import GetAgentInput, GetAgentOutput, Input, Output
# Custom imports below
from insightconnect_plugin_runtime.helper import clean
from threatstack.errors import ThreatStackAPIError, ThreatStackClientError, APIRateLimitError
from insightconnect_plugin_runtime.exceptions import PluginException


class GetAgent(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_agent',
                description='Get agent data',
                input=GetAgentInput(),
                output=GetAgentOutput())

    def run(self, params={}):
        agent_id = params.get(Input.AGENT_ID)

        try:
            agent = clean(self.connection.client.agents.get(agent_id))
        except (ThreatStackAPIError, ThreatStackClientError, APIRateLimitError) as e:
            raise PluginException(cause="An error occurred!",
                                  assistance=e)

        return {Output.AGENT: agent}
