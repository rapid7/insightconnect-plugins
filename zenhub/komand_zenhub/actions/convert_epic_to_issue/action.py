import komand
from .schema import ConvertEpicToIssueInput, ConvertEpicToIssueOutput
# Custom imports below
import json


class ConvertEpicToIssue(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='convert_epic_to_issue',
                description='Convert a ZenHub Epic back to a GitHub Issue',
                input=ConvertEpicToIssueInput(),
                output=ConvertEpicToIssueOutput())

    def run(self, params={}):
        esponse = self.connection.request(
            'POST', ('repositories', params.get('repo_id'),
                     'epics', params.get('epic_id'), 'convert_to_issue')
        )
        if response.ok:
            return {'status_code': response.status_code}
        else:
            self.logger.error('ZenHub API: ' + response.json().get('message', ''))
            response.raise_for_status()

    def test(self):
        return self.connection.test()
