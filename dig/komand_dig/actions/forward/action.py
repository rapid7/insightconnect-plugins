import komand
from .schema import ForwardInput, ForwardOutput, Input, Output, Component
import re
from komand_dig.util import util


class Forward(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='forward',
            description=Component.DESCRIPTION,
            input=ForwardInput(),
            output=ForwardOutput())

    def run(self, params={}):
        if len(params.get(Input.RESOLVER, '')) > 0:
            cmd = f"@{params.get(Input.RESOLVER)} {params.get(Input.DOMAIN)} {params.get(Input.QUERY)}"
        else:
            cmd = f"{params.get(Input.DOMAIN)} {params.get(Input.QUERY)}"

        command_output = util.execute_command(self.logger, cmd, r'ANSWER SECTION:\n(.*)\n\n;;', re.DOTALL)
        answer_section = command_output['answer_section']
        if answer_section is None:
            ans = ['Not found']
        else:
            # Grab address
            if params[Input.QUERY] == "SOA":
                domain = util.safe_parse(re.search(r'SOA\t(\S+)', answer_section))
                if util.not_empty(domain):
                    domain = domain.rstrip('.')
                ans = [domain]
            else:
                ans = answer_section.split('\n')
                if len(ans) == 0:
                    ans.append('NO MATCHES FOUND')
                ans = [util.safe_parse(re.search(r'\s(\S+)$', answer)) for answer in ans]
                ans = [answer.rstrip('.') for answer in ans]

        return {
            Output.FULLOUTPUT: command_output['fulloutput'],
            Output.QUESTION: params.get(Input.DOMAIN),
            Output.NAMESERVER: command_output['nameserver'],
            Output.STATUS: command_output['status'],
            Output.ANSWER: ans[0],
            Output.LAST_ANSWER: ans[len(ans) - 1],
            Output.ALL_ANSWERS: ans
        }
