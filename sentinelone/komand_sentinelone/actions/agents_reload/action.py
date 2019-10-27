import komand
from .schema import AgentsReloadInput, AgentsReloadOutput, Input, Output, Component


class AgentsReload(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_reload',
                description=Component.DESCRIPTION,
                input=AgentsReloadInput(),
                output=AgentsReloadOutput())

    def run(self, params={}):
        return {
            Output.AFFECTED: self.connection.agents_support_action(
                "reload",
                params.get(Input.FILTER, None),
                params.get(Input.MODULE, None)
            ).get("affected", 0)
        }
