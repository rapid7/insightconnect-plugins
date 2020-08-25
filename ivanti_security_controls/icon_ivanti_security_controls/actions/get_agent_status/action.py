import insightconnect_plugin_runtime
from .schema import GetAgentStatusInput, GetAgentStatusOutput, Input, Output, Component
# Custom imports below


class GetAgentStatus(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_agent_status',
                description=Component.DESCRIPTION,
                input=GetAgentStatusInput(),
                output=GetAgentStatusOutput())

    def run(self, params={}):
        agent_status = self.connection.ivanti_api.get_agent_status(params.get(Input.ID))

        return {
            Output.AGENT_STATUS: agent_status
        }
