import komand
from .schema import AgentsInitiateInput, AgentsInitiateOutput, Input, Output, Component


class AgentsInitiate(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_initiate',
                description=Component.DESCRIPTION,
                input=AgentsInitiateInput(),
                output=AgentsInitiateOutput())

    def run(self, params={}):
        return {
            Output.AFFECTED: self.connection.agents_action("initiate-scan", params.get(Input.FILTER, "")).get("affected", 0)
        }
