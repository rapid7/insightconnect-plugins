import komand
from .schema import ForwardInput, ForwardOutput
import subprocess
import re
from komand_dig.util import util


class Forward(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='forward',
                description='Forward DNS Query',
                input=ForwardInput(),
                output=ForwardOutput())

    def run(self, params={}):
      binary = "/usr/bin/dig"

      if len(params.get('resolver', '')) > 0:
          cmd = "%s @%s %s %s" % (binary, params.get('resolver'), params.get('domain'), params.get('query'))
      else:
          cmd = "%s %s %s" % (binary, params.get('domain'), params.get('query'))

      self.logger.info("Executing command %s" % cmd)
      r = komand.helper.exec_command(cmd)

      # Grab query status
      status = util.safe_parse(re.search('status: (.+?),', r['stdout']))
      # Grab nameserver
      ns = util.safe_parse(re.search('SERVER: (.+?)#', r['stdout']))
      # Grab number of answers
      answers = util.safe_parse(re.search(r'ANSWER: ([0-9]+)', r['stdout']))
      if util.not_empty(answers) : answers = int(answers)

      # We need answers to continue
      if answers > 0:
        # Grab resolved address section

        answer_section = util.safe_parse(re.search(r'ANSWER SECTION:\n(.*)\n\n;;', r['stdout'], flags=re.DOTALL))
        # Grab address
        if params['query'] == "SOA":
          domain = util.safe_parse(re.search(r'SOA\t(\S+)', answer_section))
          if util.not_empty(domain) : domain = domain.rstrip('.')
          ans = [domain]
        else:
          ans = answer_section.split('\n')
          if len(ans) == 0:
              ans.append('NO MATCHES FOUND')
          ans = [util.safe_parse(re.search(r'\s(\S+)$', answer)) for answer in ans]
          ans = [answer.rstrip('.') for answer in ans]
      else:
        ans = ['Not found']

      if status != "NOERROR":
        r['stdout'] = 'Resolution failed, nameserver %s returned %s status' % (ns, status)
        resolved = 'Not found'

      return { 'fulloutput': r['stdout'] + r['stderr'], 'question': params.get('domain'), 'nameserver': ns, 'status': status, 'answer': ans[0], 'last_answer': ans[len(ans) - 1], 'all_answers': ans}
