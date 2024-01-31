import insightconnect_plugin_runtime
import time
import json
import requests
import queue
import datetime
import dateutil.tz
import urllib.parse

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_github.triggers.issue.schema import IssueInput, IssueOutput, Input, Output, Component

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


class Issue(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="issue", description=Component.DESCRIPTION, input=IssueInput(), output=IssueOutput()
        )
        self.list_issues = queue.Queue()
        self.omit_list = []

    def filter_issue(self, issue_dict, now_time, issue_time):
        issue_split = issue_time.split("T")
        issue_split[1] = issue_split[1].replace("Z", "")
        issue_day = issue_split[1].split(":")
        issue_year = issue_split[0]

        now_split = now_time.split("T")
        now_split[1] = now_split[1].replace("Z", "")
        now_day = now_split[1].split(":")
        now_year = now_split[0]

        if now_year == issue_year:
            for count, _value in enumerate(issue_day):
                if now_day[count] == issue_day[count] and count == 0:
                    if (int(issue_day[count]) + 1) > int(now_day[count]) and issue_dict not in self.omit_list:
                        return True
                return False
        return False

    def clean_issues(self, issues, now_time):
        issue_obj_list = []
        new_json = []
        for issue in issues:
            ts = datetime.datetime.strptime(issue["created_at"], "%Y-%m-%dT%H:%M:%SZ")
            issue_obj = {
                "url": issue.get("html_url", ""),
                "title": issue.get("title", ""),
                "body": issue.get("body", ""),
                "creation_date": datetime.datetime.strftime(ts, "%Y-%m-%d %H:%M:%S"),
                "author": issue.get("user", {}).get("login"),
            }
            for key, value in issue_obj.items():
                if value is None:
                    value = ""
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
        utc_offset = -(time.altzone if is_dst else time.timezone)
        timezone = time.tzname[time.daylight]
        time_now = str(datetime.datetime.now(dateutil.tz.tzoffset(timezone, utc_offset))).replace(" ", "T")
        self.logger.info(utc_offset)
        self.logger.info(time.timezone)
        return time_now

    def run(self, params={}):
        counter = 0
        etag_store = "Not set"
        p_rams = {"since": None}
        data = {}
        headers_store = {
            "If-None-Match": "Not set",
            "Content-Type": "application/json",
            "Accept": "application/vnd.github.v3+json; charset=utf-8",
        }

        assign = params.get(Input.ASSIGNEE)
        org = params.get(Input.ORGANIZATION)
        repo = params.get(Input.REPOSITORY)
        frequency = params.get(Input.FREQUENCY, 300)

        parsed_repo = urllib.parse.quote(repo)
        parsed_org = urllib.parse.quote(org)
        parsed_usermame = urllib.parse.quote(self.connection.username)

        if assign and org and repo:
            api_call = requests.compat.urljoin(self.connection.api_prefix, f"/repos/{parsed_org}/{parsed_repo}/issues")
            data["assignee"] = assign
            self.logger.info(f"Monitoring issues for assignee {assign} on repository {repo} in organization {org}")

        elif org and repo:
            api_call = requests.compat.urljoin(self.connection.api_prefix, f"/repos/{parsed_org}/{parsed_repo}/issues")
            self.logger.info(f"Monitoring issues for repository {repo} in organization {org}")

        elif assign and repo:
            api_call = requests.compat.urljoin(
                self.connection.api_prefix, f"/repos/{parsed_usermame}/{parsed_repo}/issues"
            )
            data["assignee"] = assign
            self.logger.info(f"Monitoring issues for assignee {assign} on repository {repo}")

        else:
            api_call = requests.compat.urljoin(
                self.connection.api_prefix, f"/repos/{parsed_usermame}/{parsed_repo}/issues"
            )
            self.logger.info(f"Monitoring issues for repository {repo}")

        while True:
            time_set_now = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%dT%H:%M:%SZ")
            p_rams["since"] = time_set_now
            time.sleep(2)
            try:
                response = self.connection.github_session.get(
                    api_call,
                    verify=True,
                    auth=(self.connection.username, self.connection.secret),
                    data=json.dumps(p_rams),
                    params=data,
                    headers=headers_store,
                )
                etag_store = response.headers.get("etag", "")
                headers_store["If-None-Match"] = etag_store
                if response.status_code == 200 and counter > 0:
                    issues = response.json()
                    issue_list = self.clean_issues(issues, time_set_now)
                    while not self.list_issues.empty():
                        for _issue in issue_list:
                            self.send({Output.ISSUE: self.list_issues.get()})
            except requests.exceptions.RequestException as error:
                raise PluginException(
                    cause="Error occoured when trying to get repo",
                    assistance="Please check that the provided inputs are correct and try again.",
                    data=error,
                )

            counter += 1
            time.sleep(frequency)
