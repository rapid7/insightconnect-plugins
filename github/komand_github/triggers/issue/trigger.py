import komand
import time
import json
import requests
import queue
import datetime
import dateutil.tz
from .schema import IssueInput, IssueOutput


requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
# Custom imports below


class Issue(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='issue',
            description='Monitor new issues',
            input=IssueInput(),
            output=IssueOutput())
        self.list_issues = queue.Queue()
        self.omit_list = []

    def filter_issue(self, issue_dict, now_time, issue_time):
        issue_split = issue_time.split('T')
        issue_split[1] = issue_split[1].replace('Z', '')
        issue_day = issue_split[1].split(':')
        issue_year = issue_split[0]

        now_split = now_time.split('T')
        now_split[1] = now_split[1].replace('Z', '')
        now_day = now_split[1].split(':')
        now_year = now_split[0]

        if now_year == issue_year:
            for i in range(0,len(issue_day)):
                if now_day[i] == issue_day[i] and i == 0:
                    if (int(issue_day[i]) + 1) > int(now_day[i]) and issue_dict not in self.omit_list:
                        return True
                return False
        return False

    def clean_issues(self, issues, now_time):
        issue_obj_list = []
        new_json = []
        for issue in issues:
            ts = datetime.datetime.strptime(issue['created_at'], "%Y-%m-%dT%H:%M:%SZ")
            issue_obj = {
                "url": issue['html_url'],
                "title": issue['title'],
                "body": issue['body'],
                "creation_date": datetime.datetime.strftime(ts, "%Y-%m-%d %H:%M:%S"),
                "author": issue['user']['login']
            }
            for key, value in issue_obj.items():
                if value is None:
                    value = ''
                new_json.append((key, value))
            output = json.dumps(dict(new_json))
            issue_raw = json.loads(output)
            ts_compare = datetime.datetime.strftime(ts, "%Y-%m-%dT%H:%M:%SZ")
            if self.filter_issue(issue_raw, now_time, ts_compare):
                self.list_issues.put(issue_raw)
                issue_obj_list.append(issue_raw)
                self.omit_list.append(issue_raw)
            issue_obj_list.reverse()
        return issue_obj_list

    def time_set(self):
        is_dst = time.daylight and time.localtime().tm_isdst > 0
        utc_offset = - (time.altzone if is_dst else time.timezone)
        timezone = time.tzname[time.daylight]
        time_now = str(datetime.datetime.now(dateutil.tz.tzoffset(timezone, utc_offset))).replace(' ', 'T')
        self.logger.info(utc_offset)
        self.logger.info(time.timezone)
        return time_now

    def run(self, params={}):
        #init time , repo, issues
        counter = 0
        etag_store = 'Not set'
        p_rams = {
            'since': None#,
            #'assignee': '*',
            #'direction': 'asc'
            #'filter': 'all'
        }
        data =  {}
        headers_store = {
            'If-None-Match': 'Not set',
            'Content-Type': 'application/json',
            'Accept': 'application/vnd.github.v3+json; charset=utf-8'}
        assign = params.get('assignee')
        org    = params.get('organization')
        repo   = params.get('repository')
        if assign and org and repo:
            api_call = self.connection.api_prefix + '/repos/' + org + '/' + repo + '/issues'
            data['assignee'] = assign
            self.logger.info('Monitoring issues for assignee %s on repository %s in organization %s', assign, repo, org)
        elif org and repo:
            api_call = self.connection.api_prefix + '/repos/' + org + '/' + repo + '/issues'
            self.logger.info('Monitoring issues for repository %s in organization %s', repo, org)
        elif assign and repo:
            api_call = self.connection.api_prefix + '/repos/' + self.connection.username + '/' + repo + '/issues'
            data['assignee'] = assign
            self.logger.info('Monitoring issues for assignee %s on repository %s', assign, repo)
        else:
            api_call = self.connection.api_prefix + '/repos/' + self.connection.username + '/' + repo + '/issues'
            self.logger.info('Monitoring issues for repository %s', repo)

        while True:
            time_set_now = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%dT%H:%M:%SZ")
            p_rams['since'] = time_set_now
            time.sleep(2)
            try:
                #self.logger.info('In loop.. Etag:' + str(headers_store))
                response = self.connection.github_session.get(api_call,
                                                              verify=True,
                                                              auth=(self.connection.username, self.connection.secret),
                                                              data=json.dumps(p_rams),
                                                              params=data,
                                                              headers=headers_store)
                #self.logger.info(response.status_code)
                #self.logger.info(response.url)
                etag_store = response.headers.get('etag')
                headers_store["If-None-Match"] = etag_store
                if response.status_code == 200 and counter > 0:
                    issues = response.json()
                    issue_list = self.clean_issues(issues, time_set_now)
                    while not self.list_issues.empty():
                        for i in issue_list:
                            #self.logger.info(i)
                            self.send({'issues': self.list_issues.get()})
            except requests.exceptions.RequestException as e:
                raise e

            counter += 1
            time.sleep(params.get('frequency', 300))
