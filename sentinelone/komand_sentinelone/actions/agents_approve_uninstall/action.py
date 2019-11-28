import komand
from .schema import AgentsApproveUninstallInput, AgentsApproveUninstallOutput, Input, Output, Component
# Custom imports below


class AgentsApproveUninstall(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_approve_uninstall',
                description=Component.DESCRIPTION,
                input=AgentsApproveUninstallInput(),
                output=AgentsApproveUninstallOutput())

    def run(self, params={}):
        return {
            Output.AFFECTED: self.connection.agents_action("approve-uninstall", params.get(Input.FILTER, None)).get("affected", 0)
        }
