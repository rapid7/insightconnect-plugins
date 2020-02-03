import komand
from .schema import ReverseInput, ReverseOutput, Input, Output, Component
import re
from komand_dig.util import util


class Reverse(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='reverse',
            description=Component.DESCRIPTION,
            input=ReverseInput(),
            output=ReverseOutput())

    def run(self, params={}):
        if len(params.get(Input.RESOLVER, '')) > 0:
            cmd = f"@{params.get(Input.RESOLVER)} -x {params.get(Input.ADDRESS)}"
        else:
            cmd = f"-x {params.get(Input.ADDRESS)}"

        command_output = util.execute_command(self.logger, cmd, 'ANSWER SECTION:\n(.*\n)', None)
        answer_section = command_output['answer_section']
        if answer_section is None:
            address = 'Not found'
        else:
            # Grab address
            address = util.safe_parse(re.search(r'\s(\S+)\n', answer_section))
            if util.not_empty(address):
                address = address.rstrip('.')

        return {
            Output.FULLOUTPUT: command_output['fulloutput'],
            Output.QUESTION: params.get(Input.ADDRESS),
            Output.NAMESERVER: command_output['nameserver'],
            Output.STATUS: command_output['status'],
            Output.ANSWER: address
        }
