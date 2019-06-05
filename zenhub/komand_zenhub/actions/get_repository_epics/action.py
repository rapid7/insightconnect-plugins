import komand
from .schema import GetRepositoryEpicsInput, GetRepositoryEpicsOutput
# Custom imports below
import json
from komand_zenhub.util import helper


class GetRepositoryEpics(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_repository_epics',
                description='Get the ZenHub Epics for a GitHub Repository',
                input=GetRepositoryEpicsInput(),
                output=GetRepositoryEpicsOutput())

    def run(self, params={}):
        response = self.connection.request(
            'GET', ('repositories', params.get('repo_id'), 'epics')
        )
        if response.ok:
            return {'epics': list(map(
                helper.issue_reference_to_json,
                response.json().get('epic_issues', [])
            ))}
        else:
            self.logger.error('ZenHub API: ' + response.json().get('message', ''))
            response.raise_for_status()

    def test(self):
        return self.connection.test()
