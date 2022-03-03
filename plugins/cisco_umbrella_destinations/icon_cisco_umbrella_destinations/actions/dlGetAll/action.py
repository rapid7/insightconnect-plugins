import insightconnect_plugin_runtime
from .schema import DlGetAllInput, DlGetAllOutput, Input, Output, Component
from typing import Any, Dict
from icon_cisco_umbrella_destinations.util.api import return_non_empty

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
        result = self.connection.client.get_destination_lists().get("data", [])
        result = [return_non_empty(element) for element in result]
        return {Output.DATA: result}
