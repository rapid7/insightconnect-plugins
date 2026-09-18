import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import CreateControlSetInput, CreateControlSetOutput, Input, Output, Component

# Custom imports below


class CreateControlSet(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_control_set",
            description=Component.DESCRIPTION,
            input=CreateControlSetInput(),
            output=CreateControlSetOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        record = params.get(Input.RECORD)
        # END INPUT BINDING - DO NOT REMOVE
        return {Output.CONTROL_SET: self.connection.client.create_record("ControlSets", record)}
