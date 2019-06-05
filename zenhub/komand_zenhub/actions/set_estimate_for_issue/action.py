import komand
from .schema import SetEstimateForIssueInput, SetEstimateForIssueOutput
# Custom imports below
import json


class SetEstimateForIssue(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='set_estimate_for_issue',
                description='Set the ZenHub Estimate Value for a GitHub Issue',
                input=SetEstimateForIssueInput(),
                output=SetEstimateForIssueOutput())

    def run(self, params={}):
        response = self.connection.request(
            'PUT', ('repositories', params.get('repo_id'),
                     'issues', params.get('issue_number'), 'estimate'),
            json={'estimate': params.get('estimate_value')}
        )
        if response.ok:
            return {
                'status_code': response.status_code,
                'estimate_value': response.json().get('estimate', -1)
            }
        else:
            self.logger.error('ZenHub API: ' + response.json().get('message', ''))
            response.raise_for_status()

    def test(self):
        return self.connection.test()
