import insightconnect_plugin_runtime
from .schema import CheckServerStatusInput, CheckServerStatusOutput, Output, Component

# Custom imports below


class CheckServerStatus(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="check_server_status",
            description=Component.DESCRIPTION,
            input=CheckServerStatusInput(),
            output=CheckServerStatusOutput(),
        )

    def run(self, params={}):
        is_server_online = self.connection.api.server_online()
        return {Output.ONLINE: is_server_online.get("online", "")}
