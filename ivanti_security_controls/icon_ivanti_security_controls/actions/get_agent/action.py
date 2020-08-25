import insightconnect_plugin_runtime
from .schema import GetAgentInput, GetAgentOutput, Input, Output, Component
# Custom imports below


class GetAgent(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_agent',
                description=Component.DESCRIPTION,
                input=GetAgentInput(),
                output=GetAgentOutput())

    def run(self, params={}):
        agent = self.connection.ivanti_api.get_agent(params.get(Input.ID))

        return {
            Output.AGENT: agent
        }
