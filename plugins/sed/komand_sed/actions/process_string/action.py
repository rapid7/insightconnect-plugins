import insightconnect_plugin_runtime
from .schema import ProcessStringInput, ProcessStringOutput, Input, Output

# Custom imports below
from komand_sed.util.helper import Helper
from komand_sed.util.constants import DEFAULT_ENCODING


class ProcessString(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="process_string",
            description="Process string",
            input=ProcessStringInput(),
            output=ProcessStringOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        input_string = params.get(Input.STRING, "").encode()
        expression = params.get(Input.EXPRESSION, "")
        options = params.get(Input.OPTIONS, "")
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.OUTPUT: Helper().process(input_string, expression, options).decode(DEFAULT_ENCODING)}
