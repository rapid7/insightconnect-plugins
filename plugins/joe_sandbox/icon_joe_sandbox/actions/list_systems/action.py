import insightconnect_plugin_runtime
from .schema import ListSystemsInput, ListSystemsOutput, Output, Component

# Custom imports below


class ListSystems(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_systems",
            description=Component.DESCRIPTION,
            input=ListSystemsInput(),
            output=ListSystemsOutput(),
        )

    def run(self):
        systems = self.connection.api.server_systems()
        return {Output.SYSTEMS: systems}
