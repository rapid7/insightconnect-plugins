import komand
from .schema import ProcessBytesInput, ProcessBytesOutput, Input, Output
# Custom imports below
from komand_sed.util.helper import Helper
import base64


class ProcessBytes(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='process_bytes',
                description='Process bytes of base64 encoded string',
                input=ProcessBytesInput(),
                output=ProcessBytesOutput())

    def run(self, params={}):
        input_str = base64.b64decode(params.get(Input.BYTES))
        sed_list = params.get(Input.EXPRESSION)
        sed_opts = params.get(Input.OPTIONS)

        return {
            Output.OUTPUT: base64.b64encode(Helper.process(input_str, sed_list, sed_opts)).decode("utf-8")
        }
