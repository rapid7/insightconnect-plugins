import insightconnect_plugin_runtime
from .schema import SeachAgentsInput, SeachAgentsOutput, Input, Output, Component
# Custom imports below


class SeachAgents(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='seach_agents',
                description=Component.DESCRIPTION,
                input=SeachAgentsInput(),
                output=SeachAgentsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
