import insightconnect_plugin_runtime
from .schema import DAddInput, DAddOutput, Input, Output, Component


# Custom imports below


class DAdd(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="dAdd",
            description=Component.DESCRIPTION,
            input=DAddInput(),
            output=DAddOutput(),
        )

    def run(self, params={}):
        dl_id = params.get(Input.DESTINATIONLISTID)
        payload = params.get(Input.PAYLOAD)

        return {Output.SUCCESS: self.connection.client.create_destinations(destination_list_id=dl_id, data=payload)}
