import komand
from .schema import ProcessFileInput, ProcessFileOutput, Input, Output
# Custom imports below
import base64
from komand_awk.util import utils


class ProcessFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='process_file',
                description='Process file with Awk',
                input=ProcessFileInput(),
                output=ProcessFileOutput())

    def run(self, params={}):
        text = base64.b64decode(params.get(Input.DATA))
        expression = utils.preprocess_expression(params.get(Input.EXPRESSION))
        out = utils.process_lines(self.logger, text, expression)
        return {
            Output.OUT: out.decode('utf-8')
        }

    def test(self):
        data = "aGVsbG8gdGhlcmUgaGVsbG8gaGUgc2VzaCBhb3VlIHN0aGFzb2VzdCAnLixwdGVvb28n"
        text = base64.b64decode(data)
        expression = utils.preprocess_expression("'{print $2}'")
        processed_lines = utils.process_lines(self.logger, text, expression).decode('utf-8')
        return {
            Output.OUT: processed_lines == "there\n"
        }
