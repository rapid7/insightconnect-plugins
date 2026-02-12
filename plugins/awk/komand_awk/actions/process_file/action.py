import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import ProcessFileInput, ProcessFileOutput, Input, Output

# Custom imports below
import base64
from komand_awk.util import utils
from komand_awk.util.constants import DEFAULT_ENCODING


class ProcessFile(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="process_file",
            description="Process file with Awk",
            input=ProcessFileInput(),
            output=ProcessFileOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        data = params.get(Input.DATA, "")
        expression = params.get(Input.EXPRESSION, "")
        # END INPUT BINDING - DO NOT REMOVE

        # Decode base64 data
        try:
            text = base64.b64decode(data)
        except Exception as error:
            raise PluginException(
                cause="Failed to decode base64 data.",
                assistance="The input data could not be decoded from base64. Please verify the data is properly base64 encoded.",
                data=error,
            )

        # Preprocess and validate expression
        expression = utils.preprocess_expression(expression)

        # Process with AWK (validation happens inside process_lines)
        out = utils.process_lines(self.logger, text, expression)

        # Decode output
        return {Output.OUT: out.decode(DEFAULT_ENCODING, errors="ignore")}
