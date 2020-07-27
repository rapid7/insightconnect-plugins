import komand
from .schema import GetAgentInput, GetAgentOutput, Input, Output
# Custom imports below
from komand.helper import clean
from threatstack.errors import ThreatStackAPIError, ThreatStackClientError, APIRateLimitError
from komand.exceptions import PluginException


class GetAgent(komand.Action):

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
