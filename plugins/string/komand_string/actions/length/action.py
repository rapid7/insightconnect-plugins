import insightconnect_plugin_runtime
from .schema import LengthInput, LengthOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class Length(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="length",
            description=Component.DESCRIPTION,
            input=LengthInput(),
            output=LengthOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        input_string = params.get(Input.STRING)
        # END INPUT BINDING - DO NOT REMOVE

        try:
            return {Output.LENGTH: len(input_string)}
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
