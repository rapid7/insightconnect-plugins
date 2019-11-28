import komand
from .schema import AgentsUpdateSoftwareInput, AgentsUpdateSoftwareOutput, Input, Output, Component
# Custom imports below


class AgentsUpdateSoftware(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_update_software',
                description=Component.DESCRIPTION,
                input=AgentsUpdateSoftwareInput(),
                output=AgentsUpdateSoftwareOutput())

    def run(self, params={}):
        return {
            Output.AFFECTED: self.connection.agents_action_with_data("update-software", params.get(Input.FILTER, None), params.get(Input.DATA, None)).get("affected", 0)
        }
