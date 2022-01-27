import insightconnect_plugin_runtime
from .schema import DDeleteInput, DDeleteOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class DDelete(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="dDelete",
            description=Component.DESCRIPTION,
            input=DDeleteInput(),
            output=DDeleteOutput(),
        )

    def run(self, params={}):
        destination_list_id = params.get(Input.DESTINATIONLISTID)
        payload = params.get(Input.PAYLOAD)

        return {
            Output.SUCCESS: self.connection.client.delete_destinations(
                destination_list_id=destination_list_id, data=payload
            )
        }
