import komand
from .schema import CheckForSquattersInput, CheckForSquattersOutput
# Custom imports below
import json
import subprocess
import shutil
import tempfile
from komand_typo_squatter.util import utils


class CheckForSquatters(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check_for_squatters',
                description='Look for potential typo squatters',
                input=CheckForSquattersInput(),
                output=CheckForSquattersOutput())

    def run(self, params={}):
        domain = params.get('domain')
        flag = "" if not params.get('flag') else (params.get('flag') if params.get('flag')[0:2] == "--" else "--" + params.get('flag'))
        path = tempfile.mkdtemp() + "/"
        fname = "results.json"
        cmd = "./dnstwist/dnstwist.py --json %s %s > %s"%(flag, domain, path + fname) if flag else "./dnstwist/dnstwist.py --json  %s > %s"%(domain, path + fname)
        self.logger.info("Running command: %s"%cmd)
        subprocess.call(cmd, shell=True)

        j = ""
        with open(path+fname,'r') as f:
            j = f.read()
        js = json.loads(j)
        for i,item in enumerate(js):
            js[i]['phishing_score'] = utils.score_domain(js[i]['domain-name'])
        shutil.rmtree(path)
        return {"potential_squatters": js}

    def test(self, params={}):
        
        return {"potential_squatters": []}
