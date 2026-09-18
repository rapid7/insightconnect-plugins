import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetControlSetInput, GetControlSetOutput, Input, Output, Component

# Custom imports below


class GetControlSet(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_control_set",
            description=Component.DESCRIPTION,
            input=GetControlSetInput(),
            output=GetControlSetOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        id = params.get(Input.ID)
        select = params.get(Input.SELECT)
        # END INPUT BINDING - DO NOT REMOVE
        return {Output.CONTROL_SET: self.connection.client.get_record("ControlSets", id, select=select)}
