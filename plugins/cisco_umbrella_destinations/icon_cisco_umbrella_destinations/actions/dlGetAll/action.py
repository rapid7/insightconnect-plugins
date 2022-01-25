import insightconnect_plugin_runtime
from .schema import DlGetAllInput, DlGetAllOutput, Input, Output, Component

# Custom imports below


class DlGetAll(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="dlGetAll",
            description=Component.DESCRIPTION,
            input=DlGetAllInput(),
            output=DlGetAllOutput(),
        )

    def run(self, _params=None):
        return {Output.SUCCESS: self.connection.client.get_destination_lists()}
