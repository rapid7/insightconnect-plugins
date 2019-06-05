import komand
from .schema import RootcheckParseInput, RootcheckParseOutput
# Custom imports below
import json
import re


class RootcheckParse(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='rootcheck_parse',
                description='Parse OSSEC Rootcheck alerts',
                input=RootcheckParseInput(),
                output=RootcheckParseOutput())

    def run(self, params={}):
        alert = params.get('alert')
        rootcheck={}
        alerts = alert.splitlines()

        # Use these to keep track of action logs with the alert
        count = len(alerts)
        num = 0
        
        for i in alerts:
            if '** Alert' in i:
                # i = '** Alert 1475146364.5660: - ossec,rootcheck'
                rootcheck['alert_id'] = float(i[9:24])
                rootcheck['category'] = i[i.find('-')+2:]
                num = num + 1
            if '->rootcheck' in i:
                # i = '2016 Sep 29 10:52:44 (komand.dev.komand.local2) any->rootcheck'
                rootcheck['timestamp'] = i[0:i.find('(')-1]
                rootcheck['agent'] = i[i.find('(')+1:i.find(')')]
                num = num + 1
            if 'Rule:' in i:
                # i = "Rule: 1200 (level 12) -> 'Integrity checksum changed.'"
                rootcheck['rule_id'] = int(re.compile('Rule: (\d+) ').match(i).group(1))
                rootcheck['level'] = int(i[i.find('(')+1:i.find(')')][6:])
                rootcheck['rule_name'] = i[i.find("'")+1:i.rfind("'")]
                num = num + 1

        log = alert.splitlines()[-1]
        rootcheck['log'] = log
        rootcheck['file'] = log[log.find("'")+1:log.rfind("'")]

        if ' ' in rootcheck['file']:
            try:
                rootcheck['file'] = re.search(r'File: (\S+)', i).group(1)
            except AttributeError:
                rootcheck['file'] = 'None'
                pass

        rootcheck['logs'] = alerts[num-count:]

        return { 'alert': rootcheck }

    def test(self):
        # TODO: Implement test function
        return {}
