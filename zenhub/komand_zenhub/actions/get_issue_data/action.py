import komand
from .schema import GetIssueDataInput, GetIssueDataOutput
# Custom imports below
from komand_zenhub.util import helper
import json


class GetIssueData(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_issue_data',
                description='Get the ZenHub Data for a GitHub Issue',
                input=GetIssueDataInput(),
                output=GetIssueDataOutput())

    def run(self, params={}):
        repo_id = params.get('repo_id')
        issue_number = params.get('issue_number')
        response = self.connection.request(
            'GET', ('repositories', repo_id, 'issues', issue_number)
        )
        if response.ok:
            return {'data': helper.issue_data_to_json(
                response.json(),
                {'repo_id': repo_id, 'issue_number': issue_number}
            )}
        else:
            self.logger.error('ZenHub API: ' + response.json().get('message', ''))
            response.raise_for_status()

    def test(self):
        return self.connection.test()
