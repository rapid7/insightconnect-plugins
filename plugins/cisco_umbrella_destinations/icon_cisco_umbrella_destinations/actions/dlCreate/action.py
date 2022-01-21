import insightconnect_plugin_runtime
from .schema import DlCreateInput, DlCreateOutput, Input, Output, Component

# Custom imports below


class DlCreate(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="dlCreate",
            description=Component.DESCRIPTION,
            input=DlCreateInput(),
            output=DlCreateOutput(),
        )

    def run(self, params={}):
        payload = params.get(Input.PAYLOAD)
        result = self.connection.client.create_destination_list(data=payload)
        newResult = {k: v for k, v in result.items() if v is not None}
        return {Output.SUCCESS: newResult}
