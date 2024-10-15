import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import Component, Input, MaxInput, MaxOutput, Output

# Custom imports below


class Max(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="max", description=Component.DESCRIPTION, input=MaxInput(), output=MaxOutput()
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        numbers = params.get(Input.NUMBERS, [])
        # END INPUT BINDING - DO NOT REMOVE

        try:
            return {Output.MAX: max(numbers)}
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
