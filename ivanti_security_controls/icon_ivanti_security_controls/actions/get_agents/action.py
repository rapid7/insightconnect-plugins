import insightconnect_plugin_runtime
from .schema import GetAgentsInput, GetAgentsOutput, Input, Output, Component
# Custom imports below


class GetAgents(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_agents',
                description=Component.DESCRIPTION,
                input=GetAgentsInput(),
                output=GetAgentsOutput())

    def run(self, params={}):
        listening = params.get(Input.LISTENING_FILTER)
        name = params.get(Input.NAME_FILTER)

        agents = self.connection.ivanti_api.get_agents(listening=listening, name=name)

        return {
            Output.COUNT: len(agents),
            Output.AGENTS: agents
        }
