import insightconnect_plugin_runtime
from .schema import AgentsAbortScanInput, AgentsAbortScanOutput, Input, Output, Component


class AgentsAbortScan(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_abort_scan',
                description=Component.DESCRIPTION,
                input=AgentsAbortScanInput(),
                output=AgentsAbortScanOutput())

    def run(self, params={}):
        response = self.connection.agents_action("abort-scan", params.get(Input.FILTER, ""))

        affected = 0
        if response.get("data"):
            affected = response.get("data").get("affected", 0)

        return {
            Output.AFFECTED: affected
        }
