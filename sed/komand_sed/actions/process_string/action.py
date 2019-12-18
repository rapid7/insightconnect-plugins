import komand
from .schema import ProcessStringInput, ProcessStringOutput, Input, Output
# Custom imports below
from komand_sed.util.helper import Helper


class ProcessString(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='process_string',
                description='Process string',
                input=ProcessStringInput(),
                output=ProcessStringOutput())

    def run(self, params={}):
        input_str = params.get(Input.STRING).encode()
        sed_list = params.get(Input.EXPRESSION)
        sed_opts = params.get(Input.OPTIONS)

        return {
            Output.OUTPUT: Helper.process(input_str, sed_list, sed_opts).decode("utf-8")
        }
