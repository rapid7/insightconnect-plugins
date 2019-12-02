import komand
from .schema import AgentsAbortScanInput, AgentsAbortScanOutput, Input, Output, Component


class AgentsAbortScan(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_abort_scan',
                description=Component.DESCRIPTION,
                input=AgentsAbortScanInput(),
                output=AgentsAbortScanOutput())

    def run(self, params={}):
        return {
            Output.AFFECTED: self.connection.agents_action("abort-scan", params.get(Input.FILTER, "")).get("affected", 0)
        }
