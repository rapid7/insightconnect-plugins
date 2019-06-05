import komand
from .schema import MoveIssueBetweenPipelinesInput, MoveIssueBetweenPipelinesOutput
# Custom imports below
import json


class MoveIssueBetweenPipelines(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='move_issue_between_pipelines',
                description='Move a Github Issue between ZenHub Pipelines',
                input=MoveIssueBetweenPipelinesInput(),
                output=MoveIssueBetweenPipelinesOutput())

    def run(self, params={}):
        position = params.get('position')
        if position == -1:
            position = 'bottom'
        response = self.connection.request(
            'POST', ('repositories', params.get('repo_id'),
                     'issues', params.get('issue_number'), 'moves'),
            json={'pipeline_id': params.get('pipeline_id'), 'position': position}
        )
        if response.ok:
            return {'status_code': response.status_code}
        else:
            response.raise_for_status()

    def test(self):
        return self.connection.test()
