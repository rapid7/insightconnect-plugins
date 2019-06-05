import komand
from .schema import AlertParseInput, AlertParseOutput
# Custom imports below
import json
import re

class AlertParse(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='alert_parse',
                description='Parse OSSEC Alert alerts',
                input=AlertParseInput(),
                output=AlertParseOutput())

    def run(self, params={}):
        alert = params.get('alert')
        alert_alert={}
        alerts = alert.splitlines()

        # Use these to keep track of action logs with the alert
        count = len(alerts)
        num = 0

        for i in alerts:
            if '** Alert' in i:
                # i = '** Alert 1475146364.5660: - ossec,alert_alert'
                alert_alert['alert_id'] = float(i[9:24])
                alert_alert['category'] = i[i.find('-')+2:]
                num = num + 1
            if '->/' in i:
                # i = '2016 Sep 29 10:52:44 (komand.dev.komand.local2) any->alert_alert'
                alert_alert['timestamp'] = i[0:i.find('(')-1]
                alert_alert['agent'] = i[i.find('(')+1:i.find(')')]
                num = num + 1
            if 'Rule:' in i:
                # i = "Rule: 1200 (level 12) -> 'Integrity checksum changed.'"
                alert_alert['rule_id'] = int(re.compile('Rule: (\d+) ').match(i).group(1))
                alert_alert['level'] = int(i[i.find('(')+1:i.find(')')][6:])
                alert_alert['rule_name'] = i[i.find("'")+1:i.rfind("'")]
                num = num + 1
            if 'Src IP: ' in i:
                # i = 'Src IP: 116.31.116.16'
                alert_alert['source_ip'] = i.split(':')[1].strip(' ')
                num = num + 1
            if 'User: ' in i:
                # i = 'User: root'
                alert_alert['user'] = i.split(':')[1].strip(' ')
                num = num + 1

        alert_alert['logs'] = alerts[num-count:]

        items = [ 'source_ip', 'user' ]
        for i in items:
            if i not in alert_alert:
                alert_alert[i] = 'Unknown'


    def test(self):
        # TODO: Implement test function
        return {}
