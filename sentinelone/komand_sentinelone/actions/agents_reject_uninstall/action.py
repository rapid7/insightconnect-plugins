import komand
from .schema import AgentsRejectUninstallInput, AgentsRejectUninstallOutput, Input, Output, Component
# Custom imports below


class AgentsRejectUninstall(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_reject_uninstall',
                description=Component.DESCRIPTION,
                input=AgentsRejectUninstallInput(),
                output=AgentsRejectUninstallOutput())

    def run(self, params={}):
        return {
            Output.AFFECTED: self.connection.agents_action("reject-uninstall", params.get(Input.FILTER, None)).get("affected", 0)
        }
