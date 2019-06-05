import komand
import time
from .schema import IssueInput, IssueOutput
# Custom imports below
import json
import requests
import queue
import datetime
import dateutil.tz


requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


class Issue(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='issue',
            description='Monitor new issues',
            input=IssueInput(),
            output=IssueOutput())
        self.list_issues = queue.Queue()

    def clean_issues(self, issues):
        issue_obj_list = []
        new_json = []
        for issue in issues:
            ts = datetime.datetime.strptime(issue['created_at'], "%Y-%m-%dT%H:%M:%SZ")
            issue_obj = {
                "url": issue['html_url'],
                "title": issue['title'],
                "body": issue['body'],
                "creation_date": datetime.datetime.strftime(ts, "%Y-%m-%d %H:%M:%SZ"),
                "author": issue['user']['login']
            }
            for key, value in issue_obj.items():
                if value is None:
                    value = ''
                new_json.append((key, value))
            output = json.dumps(dict(new_json))
            issue_raw = json.loads(output)
            self.list_issues.put(issue_raw)
            issue_obj_list.append(issue_raw)
        return issue_obj_list

    def time_set(self):
        is_dst = time.daylight and time.localtime().tm_isdst > 0
        utc_offset = - (time.altzone if is_dst else time.timezone)
        timezone = time.tzname[time.daylight]
        time_now = datetime.datetime.now(dateutil.tz.tzoffset(time.tzname[time.daylight], utc_offset))
        return time_now

    def run(self, params={}):
        #init time , repo, issues
        counter = 0
        etag_store = 'Not set'
        p_rams = {
            'since': None,
            'assignee': None
        }
        headers_store = {'If-None-Match': 'Not set'}
        assign = params.get('assignee')
        org    = params.get('org')
        repo   = params.get('repository')
        if assign and org and repo:
            api_call = self.connection.api_prefix + '/repos/' + org + '/' + repo + '/issues'
            p_rams['assignee'] = assign
            self.logger.info('Monitoring issues for assignee %s on repository %s in organization %s', assign, repo, org)
        elif org and repo:
            api_call = self.connection.api_prefix + '/repos/' + org + '/' + repo + '/issues'
            self.logger.info('Monitoring issues on repository %s in organization %s', repo, org)
            p_rams['assignee'] = None
        elif assign and repo:
            api_call = self.connection.api_prefix + '/repos/' + self.connection.username + '/' + repo + '/issues'
            p_rams['assignee'] = assign
            self.logger.info('Monitoring issues for assignee %s on repository %s', assign, repo)
        else:
            api_call = self.connection.api_prefix + '/repos/' + self.connection.username + '/' + repo + '/issues'
            self.logger.info('Monitoring issues on repository %s', repo)

        while True:
            p_rams['since'] = self.time_set()
            try:
                #self.logger.info('In loop.. Etag:' + str(headers_store))
                response = requests.get(api_call,
                                        verify=False,
                                        auth = (self.connection.username, self.connection.secret),
                                        params = p_rams,
                                        headers = headers_store)
                self.logger.info(response.status_code)
                etag_store = response.headers['ETag']
                headers_store["If-None-Match"] = etag_store
                if response.status_code == 200 and counter > 0:
                    issues = response.json()
                    issue_list = self.clean_issues(issues)
                    while not self.list_issues.empty():
                        self.send({'issues': self.list_issues.get()})

            except requests.exceptions.RequestException as e:
                raise e

            counter += 1
            time.sleep(params.get('frequency', 300))


    def test(self):
        try:
            api_call = self.connection.api_prefix + '/user'
            response = requests.get(api_call, auth = (self.connection.username, self.connection.secret), verify=False)
            if response.status_code == 200:
                return {'status': 'Success'}
        except requests.exceptions.RequestException as e:
            return {'status': 'Error'}
