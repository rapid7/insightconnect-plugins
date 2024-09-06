import insightconnect_plugin_runtime
from .schema import UpperInput, UpperOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class Upper(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="upper",
            description="Converts lowercase letters to uppercase",
            input=UpperInput(),
            output=UpperOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        input_string = params.get(Input.STRING)
        # END INPUT BINDING - DO NOT REMOVE

        if not input_string:
            raise PluginException(
                cause="Action failed! Missing required user input.",
                assistance="Please provide the input string.",
            )

        try:
            return {Output.UPPER: input_string.upper()}
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
