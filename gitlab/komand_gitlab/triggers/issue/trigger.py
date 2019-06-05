import komand
import time
import json
import urllib
import requests
import datetime
from .schema import IssueInput, IssueOutput
# Custom imports below


class Issue(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='issue',
            description='Monitor new issues',
            input=IssueInput(),
            output=IssueOutput())

    def clean_json(self, obj):
        new_json = []
        for key, value in obj.items():
            if value is None:
                value = ''
            if key == 'assignee' and value == "":
                value = {}
            if key == 'milestone' and value == "":
                value = {}
            new_json.append((key, value))
        output = json.dumps(dict(new_json))
        return json.loads(output)

    def new(self, date):
        acceptable = '0:00:30.000000' # last 15 sec
        #'0:00:15.761923'
        time_now = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        time_now = datetime.datetime.strptime(time_now, '%Y-%m-%dT%H:%M:%S.%fZ')

        date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')

        differance = str(time_now - date)
        if differance > acceptable:
            return False
        return True

    def run(self, params={}):
        issues = None
        issue_params = []
        new_issues = []
        seen = []
        if params.get('milestone'):
            issue_params.append(('milestone', params.get('milestone')))
        if params.get('labels'):
            issue_params.append(('labels', params.get('labels')))
        if params.get('state'):
            issue_params.append(('state', params.get('state').lower()))
        if params.get('search'):
            issue_params.append(('search', params.get('search')))
        if params.get('iid'):
            issue_params.append(('iid', params.get('iid')))

        while True:
            self.logger.info('Searching')
            r_url = '%s/issues' % (self.connection.url)
            r_url += '?%s' % (urllib.parse.urlencode(issue_params))

            try:
                r = requests.get(r_url, headers={'PRIVATE-TOKEN': self.connection.token}, verify=False)
                if r.ok:
                    issues = r.json()
                    for issue in issues:
                        issue = self.clean_json(json.loads(json.dumps(issue)))
                        if self.new(issue['updated_at']):
                            new_issues.append(issue)
                if len(new_issues):
                    if new_issues[0] in seen:
                        a = "seen"
                    else:
                        self.send(new_issues[0])
                        seen.append(new_issues[0])
            except requests.exceptions.RequestException as e:  # This is the correct syntax
                self.logger.error(e)

            time.sleep(params.get('interval') or 5)

    def test(self):
        """TODO: Test the trigger"""
        return {}
