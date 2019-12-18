import komand
from .schema import ProcessStringInput, ProcessStringOutput, Input, Output
# Custom imports below
from komand_awk.util import utils


class ProcessString(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='process_string',
                description='Process string with Awk',
                input=ProcessStringInput(),
                output=ProcessStringOutput())

    def run(self, params={}):
        expression = utils.preprocess_expression(params.get(Input.EXPRESSION))
        out = utils.process_lines(self.logger, params.get(Input.TEXT), expression)
        return {
            Output.OUT: out.decode('utf-8')
        }

    def test(self):
        text = "hello world"
        expression = utils.preprocess_expression("'{print $2}'")
        processed_lines = utils.process_lines(self.logger, text, expression).decode('utf-8')
        return {
            Output.OUT: processed_lines == 'world\n'
        }
