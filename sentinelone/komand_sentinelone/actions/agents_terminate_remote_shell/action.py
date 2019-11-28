import komand
from .schema import AgentsTerminateRemoteShellInput, AgentsTerminateRemoteShellOutput, Input, Output, Component


# Custom imports below


class AgentsTerminateRemoteShell(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='agents_terminate_remote_shell',
            description=Component.DESCRIPTION,
            input=AgentsTerminateRemoteShellInput(),
            output=AgentsTerminateRemoteShellOutput())

    def run(self, params={}):
        return {
            Output.AFFECTED: self.connection.agents_action_with_data(
                "terminate-remote-shell",
                params.get(Input.FILTER, None),
                {"channelId": params.get(Input.CHANNEL_ID, None)}
            ).get("affected", 0)
        }
