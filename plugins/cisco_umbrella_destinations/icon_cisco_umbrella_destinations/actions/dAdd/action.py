import insightconnect_plugin_runtime
from .schema import DAddInput, DAddOutput, Input, Output, Component
from insightconnect_plugin_runtime.helper import clean

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
        destination_list_id = params.get(Input.DESTINATIONLISTID)
        destination = params.get(Input.DESTINATION)
        comment = params.get(Input.COMMENT)

        if comment:
            data = [{"destination": destination, "comment": comment}]
        else:
            data = [{"destination": destination}]

        result = self.connection.client.create_destinations(destination_list_id=destination_list_id, data=data).get(
            "data", {}
        )

        result = clean(result)
        return {Output.SUCCESS: result}
