import komand
from .schema import AgentsFetchLogsInput, AgentsFetchLogsOutput, Input, Output, Component


class AgentsFetchLogs(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_fetch_logs',
                description=Component.DESCRIPTION,
                input=AgentsFetchLogsInput(),
                output=AgentsFetchLogsOutput())

    def run(self, params={}):
        return {
            Output.AFFECTED: self.connection.agents_action("fetch-logs", params.get(Input.FILTER, "")).get("affected", 0)
        }
