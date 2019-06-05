import komand
from .schema import ProcessFileInput, ProcessFileOutput
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
        text = base64.b64decode(params['data'])
        expression = utils.preprocess_expression(self.logger, params.get('expression'))
        out = utils.process_lines(self.logger, text, expression)
        return {'out': out.decode('utf-8') }

    def test(self):
        data = "aGVsbG8gdGhlcmUgaGVsbG8gaGUgc2VzaCBhb3VlIHN0aGFzb2VzdCAnLixwdGVvb28n"
        text = base64.b64decode(data)
        expression = " {print $2}"
        cmd = 'echo "%s" | %s \'%s\'' % (text, utils.awk, expression)
        rcode = komand.helper.exec_command(cmd)['rcode']
        return {'out': str(rcode)}
