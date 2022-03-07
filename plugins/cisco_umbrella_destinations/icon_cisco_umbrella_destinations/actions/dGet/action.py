import insightconnect_plugin_runtime
from .schema import DGetInput, DGetOutput, Input, Output, Component
from insightconnect_plugin_runtime.helper import clean

# Custom imports below


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
        result = self.connection.client.get_destinations(destination_list_id=destination_list_id).get("data", [])
        result = clean(result)
        return {Output.SUCCESS: result}
