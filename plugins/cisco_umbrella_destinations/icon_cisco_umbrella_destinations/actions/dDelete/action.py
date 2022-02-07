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

        # Convert input str 1234 5678 into format [1234, 5678]
        # x = '1234 5678'
        # x.split(" ") == ['1234', '5678']
        payload = params.get(Input.PAYLOAD).split(" ")

        payload = remove_non_numerical_characters(payload)

        return {
            Output.SUCCESS: self.connection.client.delete_destinations(
                destination_list_id=destination_list_id, data=payload
            )
        }


# This handles any characters in the IDs which are not numerical values
def remove_non_numerical_characters(payload):
    for index, i in enumerate(payload):
        numeric_filter = filter(str.isdigit, i)
        new = "".join(numeric_filter)
        payload[index] = new
    return payload
