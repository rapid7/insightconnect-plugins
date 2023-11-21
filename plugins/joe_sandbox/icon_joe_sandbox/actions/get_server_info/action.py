import insightconnect_plugin_runtime
from .schema import GetServerInfoInput, GetServerInfoOutput, Input, Output, Component
# Custom imports below


class GetServerInfo(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="get_server_info",
                description=Component.DESCRIPTION,
                input=GetServerInfoInput(),
                output=GetServerInfoOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        # END INPUT BINDING - DO NOT REMOVE
        # TODO - If input bindings for connection can be done check to same if it you can do the same here
        server_info = self.connection.api.server_info()

        return server_info
