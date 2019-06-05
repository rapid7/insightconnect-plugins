import komand
from .schema import GetIssueEventsInput, GetIssueEventsOutput
# Custom imports below
import json
from komand_zenhub.util import helper


class GetIssueEvents(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_issue_events',
                description='Get the ZenHub Events for a GitHub Issue',
                input=GetIssueEventsInput(),
                output=GetIssueEventsOutput())

    def run(self, params={}):
        response = self.connection.request(
            'GET', ('repositories', params.get('repo_id'),
                    'issues', params.get('issue_number'), 'events')
        )
        if response.ok:
            return {'events': list(map(
                helper.issue_event_to_json,
                response.json()
            ))}
        else:
            self.logger.error('ZenHub API: ' + response.json().get('message', ''))
            response.raise_for_status()

    def test(self):
        return self.connection.test()
