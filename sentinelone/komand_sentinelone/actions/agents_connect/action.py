import insightconnect_plugin_runtime
from .schema import AgentsConnectInput, AgentsConnectOutput, Input, Output, Component


class AgentsConnect(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_connect',
                description=Component.DESCRIPTION,
                input=AgentsConnectInput(),
                output=AgentsConnectOutput())

    def run(self, params={}):
        return {
            Output.AFFECTED: self.connection.agents_action("connect", params.get(Input.FILTER, "")).get("affected", 0)
        }
