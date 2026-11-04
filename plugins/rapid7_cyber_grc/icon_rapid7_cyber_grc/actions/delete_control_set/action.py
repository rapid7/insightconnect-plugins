import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import DeleteControlSetInput, DeleteControlSetOutput, Input, Output, Component

# Custom imports below


class DeleteControlSet(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_control_set",
            description=Component.DESCRIPTION,
            input=DeleteControlSetInput(),
            output=DeleteControlSetOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        record_id = params.get(Input.ID)
        # END INPUT BINDING - DO NOT REMOVE
        return {Output.RESULT: self.connection.client.delete_record("ControlSets", record_id)}
