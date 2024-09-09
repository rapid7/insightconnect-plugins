import insightconnect_plugin_runtime
from .schema import SplitToListInput, SplitToListOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class SplitToList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="split_to_list",
            description="Converts a string to a list of strings",
            input=SplitToListInput(),
            output=SplitToListOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        input_string = params.get(Input.STRING)
        delimiter = params.get(Input.DELIMITER)
        # END INPUT BINDING - DO NOT REMOVE

        if not input_string:
            raise PluginException(
                cause="Action failed! Missing required user input.",
                assistance="Please provide the input string.",
            )

        if not delimiter:
            self.logger.info("User did not supply a string delimiter. Defaulting to a newline character.")
            delimiter = "\n"

        try:
            return {Output.LIST: input_string.split(delimiter)}
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
