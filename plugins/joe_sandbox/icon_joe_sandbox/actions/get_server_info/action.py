import insightconnect_plugin_runtime
from .schema import GetServerInfoInput, GetServerInfoOutput, Output, Component

# Custom imports below


class GetServerInfo(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_server_info",
            description=Component.DESCRIPTION,
            input=GetServerInfoInput(),
            output=GetServerInfoOutput(),
        )

    def run(self):
        server_info = self.connection.api.server_info()
        return {Output.QUEUESIZE: server_info.get("queuesize")}
