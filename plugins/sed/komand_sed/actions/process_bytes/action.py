import insightconnect_plugin_runtime
from .schema import ProcessBytesInput, ProcessBytesOutput, Input, Output

# Custom imports below
from komand_sed.util.helper import Helper
from komand_sed.util.constants import DEFAULT_ENCODING
import base64


class ProcessBytes(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="process_bytes",
            description="Process bytes of base64 encoded string",
            input=ProcessBytesInput(),
            output=ProcessBytesOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        input_bytes = params.get(Input.BYTES, "").encode()
        expression = params.get(Input.EXPRESSION, "")
        options = params.get(Input.OPTIONS, "")
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.OUTPUT: base64.b64encode(Helper().process(input_bytes, expression, options)).decode(DEFAULT_ENCODING)
        }
