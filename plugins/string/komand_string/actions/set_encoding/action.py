import insightconnect_plugin_runtime
from .schema import SetEncodingInput, SetEncodingOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class SetEncoding(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="set_encoding",
            description=Component.DESCRIPTION,
            input=SetEncodingInput(),
            output=SetEncodingOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        input_string = params.get(Input.STRING)
        encoding_val = params.get(Input.ENCODING, "").lower()
        error_handler = params.get(Input.ERROR_HANDLING)
        # END INPUT BINDING - DO NOT REMOVE

        try:
            output = input_string.encode(encoding_val, error_handler)
            return {Output.ENCODED: output.decode(encoding_val, error_handler)}
        except Exception as error:
            raise PluginException(cause="Encoding failed.", assistance="Could not encode given string.", data=error)
