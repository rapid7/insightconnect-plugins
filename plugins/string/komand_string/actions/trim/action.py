import insightconnect_plugin_runtime
from .schema import TrimInput, TrimOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class Trim(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="trim", description=Component.DESCRIPTION, input=TrimInput(), output=TrimOutput()
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        input_string = params.get(Input.STRING)
        # END INPUT BINDING - DO NOT REMOVE

        try:
            return {Output.TRIMMED: input_string.strip()}
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
