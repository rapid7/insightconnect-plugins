import komand
from .schema import RemoveIssueFromEpicInput, RemoveIssueFromEpicOutput
# Custom imports below
import json


class RemoveIssueFromEpic(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='remove_issue_from_epic',
                description='Remove a GitHub Issue from a ZenHub Epic',
                input=RemoveIssueFromEpicInput(),
                output=RemoveIssueFromEpicOutput())

    def run(self, params={}):
        issue = params.get('issue')
        response = self.connection.request(
            'POST', ('repositories', params.get('repo_id'),
                     'epics', params.get('epic_id'), 'update_issues'),
            json={'remove_issues': [issue]}
        )
        if response.ok:
            return {
                'status_code': response.status_code,
                'issue': issue
            }
        else:
            self.logger.error('ZenHub API: ' + response.json().get('message', ''))
            response.raise_for_status()

    def test(self):
        return self.connection.test()
