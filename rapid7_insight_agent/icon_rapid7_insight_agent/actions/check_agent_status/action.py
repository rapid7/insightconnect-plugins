import insightconnect_plugin_runtime
from .schema import CheckAgentStatusInput, CheckAgentStatusOutput, Input, Output, Component
# Custom imports below



class CheckAgentStatus(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check_agent_status',
                description=Component.DESCRIPTION,
                input=CheckAgentStatusInput(),
                output=CheckAgentStatusOutput())

    def run(self, params={}):
        agent_id = params.get(Input.AGENT_ID)
        return self.connection.api.get_agent_status(agent_id)
