import insightconnect_plugin_runtime
from .schema import DlGetInput, DlGetOutput, Input, Output, Component

# Custom imports below


class DlGet(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="dlGet",
            description=Component.DESCRIPTION,
            input=DlGetInput(),
            output=DlGetOutput(),
        )

    def run(self, params={}):
        destination_list_id = params.get(Input.DESTINATIONLISTID)

        return {Output.SUCCESS: self.connection.client.get_destination_list(destination_list_id=destination_list_id)}
