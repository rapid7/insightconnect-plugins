import komand
from .schema import ConvertIssueToEpicInput, ConvertIssueToEpicOutput
# Custom imports below
import json


class ConvertIssueToEpic(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='convert_issue_to_epic',
                description='Convert a GitHub Issue to a ZenHub Epic',
                input=ConvertIssueToEpicInput(),
                output=ConvertIssueToEpicOutput())

    def run(self, params={}):
        response = self.connection.request(
            'POST', ('repositories', params.get('repo_id'),
                     'issues', params.get('issue_number'), 'convert_to_epic'),
            json={'issues': params.get('issues', [])}
        )
        if response.ok or response.status_code == 400:
            return {'status_code': response.status_code}
        else:
            response.raise_for_status()

    def test(self):
        return self.connection.test()
