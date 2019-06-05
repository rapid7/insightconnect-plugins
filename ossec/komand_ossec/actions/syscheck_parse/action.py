import komand
from .schema import SyscheckParseInput, SyscheckParseOutput
# Custom imports below
import json
import re


class SyscheckParse(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='syscheck_parse',
                description='Parse OSSEC Syscheck alerts',
                input=SyscheckParseInput(),
                output=SyscheckParseOutput())

    def run(self, params={}):
        alert = params.get('alert')
        syscheck={}

        for i in alert.splitlines():
            if '** Alert' in i:
                # i = '** Alert 1475146364.5660: - ossec,syscheck'
                syscheck['alert_id'] = float(i[9:24])
                syscheck['category'] = i[i.find('-')+2:]
            if '->syscheck' in i:
                # i = '2016 Sep 29 10:52:44 (komand.dev.komand.local2) any->syscheck'
                syscheck['timestamp'] = i[0:i.find('(')-1]
                syscheck['agent'] = i[i.find('(')+1:i.find(')')]
            if 'Rule:' in i:
                # i = "Rule: 1200 (level 12) -> 'Integrity checksum changed.'"
                syscheck['rule_id'] = int(re.compile('Rule: (\d+) ').match(i).group(1))
                syscheck['level'] = int(i[i.find('(')+1:i.find(')')][6:])
                syscheck['rule_name'] = i[i.find("'")+1:i.rfind("'")]
            if 'Integrity checksum changed for' in i:
                syscheck['file'] = i[i.find("'")+1:i.rfind("'")]
            if 'Size changed from' in i:
                syscheck['size_old'] = int(i.split("'")[1])
                syscheck['size_new'] = int(i.split("'")[3])
            if 'Old md5sum was' in i:
                syscheck['md5_old'] = i[i.find("'")+1:i.rfind("'")]
            if 'New md5sum is' in i:
                syscheck['md5_new'] = i[i.find("'")+1:i.rfind("'")]
            if 'Old sha1sum was' in i:
                syscheck['sha_old'] = i[i.find("'")+1:i.rfind("'")]
            if 'New sha1sum is' in i:
                syscheck['sha_new'] = i[i.find("'")+1:i.rfind("'")]
            if 'Permissions changed from' in i:
                syscheck['perms_old'] = i.split("'")[1]
                syscheck['perms_new'] = i.split("'")[3]

        items = [ 'md5_old', 'md5_new', 'sha_old', 'sha_new', 'perms_old', 'perms_new' ]
        for i in items:
            if i not in syscheck:
                syscheck[i] = 'Unknown'

        return { 'alert': syscheck }

    def test(self):
        # TODO: Implement test function
        return {}
