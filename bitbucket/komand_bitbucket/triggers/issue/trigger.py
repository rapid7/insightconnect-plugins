import komand
import time
import requests
import datetime
import urllib.parse
from komand_bitbucket.util import helpers
from komand.exceptions import PluginException

from .schema import IssueInput, IssueOutput, Input, Output, Component

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


# Custom imports below


class Issue(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='issue',
            description=Component.DESCRIPTION,
            input=IssueInput(),
            output=IssueOutput())

    def run(self, params={}):
        headers = {'If-None-Match': 'Not set', 'Content-Length': '0', 'Content-Type': 'application/json'}
        counter = 0
        omit_list = []
        q_params = ''
        issue_params = [
            ('and assignee.username = "%s"', params.get(Input.ASSIGNEE)),  # assignee username
            ('and milestone.name = "%s"', params.get(Input.MILESTONE)),  # milestone string
            ('and component.name = "%s"', params.get(Input.COMPONENT)),  # component string
            ('and version.name = "%s"', params.get(Input.VERSION)),  # version string
            ('and kind = "%s"', ('bug' if params.get(Input.KIND) == 'None' else params.get(Input.KIND)).lower()),
            # kind : 'bug, enhancement, proposal, task' - defualt = bug
            ('and priority = "%s"',
             ('major' if params.get(Input.PRIORITY) == 'None' else params.get(Input.PRIORITY)).lower()),
            # priority 'trivial, minor, major, critical, blocker' - defualt = major
            ('and state = "%s"', ('new' if params.get(Input.STATE) == 'None' else params.get(Input.STATE)).lower())
            # new, open, resolved, on hold, invalid, duplicate, wontfix, closed - defualt = new
        ]

        # Create Query String of all passed in variables
        issue_params = [(query, status) for query, status in issue_params if status]
        for ele in issue_params:
            q_params += ' ' + ele[0] % (ele[1])

        while True:
            timestamp = (datetime.datetime.strftime(datetime.datetime.utcnow(), "%Y-%m-%dT%H:%M:%S").replace(' ', 'T'))
            if int(timestamp[15]) != 0:
                timestamp = timestamp[:15] + str(int(timestamp[15]) - 1) + timestamp[16:]
            self.logger.info(timestamp)

            # delay assures offset
            time.sleep(2)
            try:
                issue_list = []
                q_string = 'created_on >= %s %s' % (timestamp, q_params)
                query = urllib.parse.urlencode({'q': q_string})
                self.connection.bucket_session.headers.update(headers)
                api_call = self.connection.base_api + f'/repositories/{self.connection.username}/{params.get(Input.REPOSITORY).lower()}/issues?{query} '
                self.logger.info(api_call)
                try:
                    response = self.connection.bucket_session.get(api_call)
                except requests.exceptions.ConnectionError:
                    time.sleep(1)
                    response = self.connection.bucket_session.get(api_call)
                etag_store = response.headers.get('etag')
                headers["If-None-Match"] = etag_store
                if response.status_code == 200 and counter > 0:
                    issues = response.json()['values']
                    for issue_item in issues:
                        issue_obj = None
                        if max(issue_item['created_on'], timestamp) == issue_item['created_on']:
                            issue_obj = helpers.clean_json({
                                'title': issue_item['title'],
                                'body': issue_item['content']['raw'],
                                'url': issue_item['links']['self']['href']
                            })

                        if issue_obj not in omit_list:
                            issue_list.append(issue_obj)
                            omit_list.append(issue_obj)
                    if issue_list:
                        self.logger.info(f"founded issue count: {issue_list}")
                        for issue in issue_list:
                            self.send({Output.ISSUES: issue})

                if response.status_code >= 400:
                    error = response.json()
                    raise PluginException(
                        cause='Server response error',
                        assistance=error['error']['message']
                    )

            except requests.exceptions.RequestException as e:
                raise PluginException(
                    cause='Server error',
                    data=e
                )

            counter += 1
            time.sleep(params.get('poll', 300))
