import insightconnect_plugin_runtime
from .schema import ReplaceInput, ReplaceOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class Replace(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="replace", description=Component.DESCRIPTION, input=ReplaceInput(), output=ReplaceOutput()
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        input_string = params.get(Input.IN_STRING)
        find_string = params.get(Input.STRING_PART_TO_FIND)
        replace_string = params.get(Input.REPLACEMENT_VALUE, "")
        # END INPUT BINDING - DO NOT REMOVE

        self.logger.info(f"in_string: {input_string}")
        self.logger.info(f"find_string: {find_string}")
        self.logger.info(f"replace_string: {replace_string}")

        try:
            return {Output.RESULT_STRING: input_string.replace(find_string, replace_string)}
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
