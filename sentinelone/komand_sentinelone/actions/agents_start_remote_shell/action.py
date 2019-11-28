import komand
from .schema import AgentsStartRemoteShellInput, AgentsStartRemoteShellOutput, Input, Output, Component
# Custom imports below


class AgentsStartRemoteShell(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_start_remote_shell',
                description=Component.DESCRIPTION,
                input=AgentsStartRemoteShellInput(),
                output=AgentsStartRemoteShellOutput())

    def run(self, params={}):
        return {
            Output.AFFECTED: self.connection.agents_action_with_data(
                "start-remote-shell",
                params.get(Input.FILTER, None),
                {
                    "columns": params.get(Input.COLUMNS),
                    "rows": params.get(Input.ROWS),
                    "historyPassword": params.get(Input.HISTORY_PASSWORD),
                    "twoFaCode": params.get(Input.TWO_FA_CODE),
                }
            ).get("affected", 0)
        }
