import insightconnect_plugin_runtime
from .schema import AgentsFetchLogsInput, AgentsFetchLogsOutput, Input, Output, Component


class AgentsFetchLogs(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_fetch_logs',
                description=Component.DESCRIPTION,
                input=AgentsFetchLogsInput(),
                output=AgentsFetchLogsOutput())

    def run(self, params={}):
        response = self.connection.agents_action("fetch-logs", params.get(Input.FILTER, ""))

        affected = response.get("data", {}).get("affected", 0)

        return {
            Output.AFFECTED: affected
        }
