import insightconnect_plugin_runtime
from .schema import DGetInput, DGetOutput, Input, Output, Component


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

        return {Output.SUCCESS: self.connection.client.get_destinations(destination_list_id=destination_list_id)}
