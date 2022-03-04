import insightconnect_plugin_runtime
from .schema import DGetInput, DGetOutput, Input, Output, Component


# Custom imports below
from icon_cisco_umbrella_destinations.util.api import return_non_empty


class DGet(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="dGet",
            description=Component.DESCRIPTION,
            input=DGetInput(),
            output=DGetOutput(),
        )

    def run(self, params={}):
        destination_list_id = params.get(Input.DESTINATIONLISTID)
        result = self.connection.client.get_destinations(destination_list_id=destination_list_id).get('data', [])
        result = [return_non_empty(element) for element in result]
        return {Output.SUCCESS: result}
