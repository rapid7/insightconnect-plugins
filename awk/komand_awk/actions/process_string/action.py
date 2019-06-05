import komand
from .schema import ProcessStringInput, ProcessStringOutput
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
        expression = utils.preprocess_expression(self.logger, params.get('expression'))
        out = utils.process_lines(self.logger, params.get('text'), expression)
        return {'out': out.decode('utf-8')}

    def test(self):
        text = "hello world"
        expression = " {print $2}"
        cmd = 'echo "%s" | %s \'%s\'' % (text, utils.awk, expression)
        rcode = komand.helper.exec_command(cmd)['rcode']
        return {'out': str(rcode)}
