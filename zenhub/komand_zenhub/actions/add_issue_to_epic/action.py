import komand
from .schema import AddIssueToEpicInput, AddIssueToEpicOutput
# Custom imports below
import json

class AddIssueToEpic(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_issue_to_epic',
                description='Add a GitHub Issue to a ZenHub Epic',
                input=AddIssueToEpicInput(),
                output=AddIssueToEpicOutput())

    def run(self, params={}):
        issue = params.get('issue')
        response = self.connection.request(
            'POST', ('repositories', params.get('repo_id'),
                     'epics', params.get('epic_id'), 'update_issues'),
            json={'add_issues': [issue]}
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
