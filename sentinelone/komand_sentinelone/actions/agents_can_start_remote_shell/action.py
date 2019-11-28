import komand
from .schema import AgentsCanStartRemoteShellInput, AgentsCanStartRemoteShellOutput, Input, Output, Component
# Custom imports below


class AgentsCanStartRemoteShell(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_can_start_remote_shell',
                description=Component.DESCRIPTION,
                input=AgentsCanStartRemoteShellInput(),
                output=AgentsCanStartRemoteShellOutput())

    def run(self, params={}):
        return {
            Output.AFFECTED: self.connection.agents_action(
                "can-start-remote-shell",
                params.get(Input.FILTER, None)
            ).get("affected", 0)
        }
