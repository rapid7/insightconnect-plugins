import insightconnect_plugin_runtime
from .schema import DlGetInput, DlGetOutput, Input, Output, Component

# Custom imports below
from icon_cisco_umbrella_destinations.util.api import return_non_empty


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
        result = self.connection.client.get_destination_list(destination_list_id=destination_list_id).get("data", {})
        result = return_non_empty(result)
        return {Output.SUCCESS: result}
