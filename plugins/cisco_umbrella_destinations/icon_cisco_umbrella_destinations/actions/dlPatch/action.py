import insightconnect_plugin_runtime
from .schema import DlPatchInput, DlPatchOutput, Input, Output, Component
from insightconnect_plugin_runtime.helper import clean

# Custom imports below


class DlPatch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="dlPatch",
            description=Component.DESCRIPTION,
            input=DlPatchInput(),
            output=DlPatchOutput(),
        )

    def run(self, params={}):
        destination_list_id = params.get(Input.DESTINATIONLISTID)
        data = {"name": params.get(Input.NAME)}
        result = self.connection.client.update_destination_list(destination_list_id=destination_list_id, data=data).get(
            "data", {}
        )
        result = clean(result)
        return {Output.SUCCESS: result}
