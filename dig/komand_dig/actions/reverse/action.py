import komand
from .schema import ReverseInput, ReverseOutput
import subprocess
import re
from komand_dig.util import util


class Reverse(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='reverse',
                description='Reverse DNS Query',
                input=ReverseInput(),
                output=ReverseOutput())

    def run(self, params={}):
        binary = "/usr/bin/dig"

        if len(params.get('resolver', '')) > 0:
            cmd = "%s @%s -x %s" % (binary, params.get('resolver'), params.get('address'))
        else:
            cmd = "%s -x %s" % (binary, params.get('address'))

        self.logger.info('Executing command %s' % cmd)
        r = komand.helper.exec_command(cmd)

        # Grab query status
        status = util.safe_parse(re.search('status: (.+?),', r['stdout']))
        # Grab nameserver
        ns = util.safe_parse(re.search('SERVER: (.+?)#', r['stdout']))
        # Grab number of answers
        answers = util.safe_parse(re.search(r'ANSWER: ([0-9]+)', r['stdout']))
        if util.not_empty(answers) : answers = int(answers)

        # We need answers to continue
        address = ""
        if answers > 0:
            # Grab address section
            answer_section = util.safe_parse(re.search(r'ANSWER SECTION:\n(.*\n)', r['stdout']))
            # Grab address
            address = util.safe_parse(re.search(r'\s(\S+)\n', answer_section))
            if util.not_empty(address) : address = address.rstrip('.')

        if status != "NOERROR":
          r['stdout'] = 'Resolution failed, nameserver %s returned %s status' % (ns, status)
          address = 'Not found'

        return { 'fulloutput': r['stdout'] + r['stderr'], 'question': params.get('address'), 'nameserver': ns, 'status': status, 'answer': address }
