import insightconnect_plugin_runtime
from .schema import UpdateAgentInput, UpdateAgentOutput, Input, Output, Component
# Custom imports below


class UpdateAgent(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_agent',
                description=Component.DESCRIPTION,
                input=UpdateAgentInput(),
                output=UpdateAgentOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
