import insightconnect_plugin_runtime
from .schema import AgentsInitiateInput, AgentsInitiateOutput, Input, Output, Component


class AgentsInitiate(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_initiate',
                description=Component.DESCRIPTION,
                input=AgentsInitiateInput(),
                output=AgentsInitiateOutput())

    def run(self, params={}):
        response = self.connection.agents_action("initiate-scan", params.get(Input.FILTER, ""))

        affected = 0
        if response.get("data"):
            affected = response.get("data").get("affected", 0)

        return {
            Output.AFFECTED: affected
        }
