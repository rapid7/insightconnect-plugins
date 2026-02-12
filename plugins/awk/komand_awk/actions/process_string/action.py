import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import ProcessStringInput, ProcessStringOutput, Input, Output

# Custom imports below
from komand_awk.util import utils
from komand_awk.util.constants import DEFAULT_ENCODING


class ProcessString(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="process_string",
            description="Process string with Awk",
            input=ProcessStringInput(),
            output=ProcessStringOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        expression = params.get(Input.EXPRESSION, "")
        text = params.get(Input.TEXT, "")
        # END INPUT BINDING - DO NOT REMOVE

        # Preprocess and validate expression
        expression = utils.preprocess_expression(expression)

        # Process with AWK (validation happens inside process_lines)
        out = utils.process_lines(self.logger, text, expression)

        # Decode output
        return {Output.OUT: out.decode(DEFAULT_ENCODING, errors="ignore")}
