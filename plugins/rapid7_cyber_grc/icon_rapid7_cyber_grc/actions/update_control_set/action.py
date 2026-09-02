import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import UpdateControlSetInput, UpdateControlSetOutput, Input, Output, Component

# Custom imports below


class UpdateControlSet(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_control_set",
            description=Component.DESCRIPTION,
            input=UpdateControlSetInput(),
            output=UpdateControlSetOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        expand = params.get(Input.EXPAND)
        id = params.get(Input.ID)
        record = params.get(Input.RECORD)
        # END INPUT BINDING - DO NOT REMOVE
        return {Output.CONTROL_SET: self.connection.client.update_record("ControlSets", id, record, expand=expand)}
