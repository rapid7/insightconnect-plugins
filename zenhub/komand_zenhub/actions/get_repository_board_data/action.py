import komand
from .schema import GetRepositoryBoardDataInput, GetRepositoryBoardDataOutput
# Custom imports below
import json
from komand_zenhub.util import helper


class GetRepositoryBoardData(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_repository_board_data',
                description='Get the ZenHub Board Data for a GitHub Repository',
                input=GetRepositoryBoardDataInput(),
                output=GetRepositoryBoardDataOutput())

    def run(self, params={}):
        repo_id = params.get('repo_id')
        response = self.connection.request(
            'GET', ('repositories', repo_id, 'board')
        )
        if response.ok:
            return {'data': helper.repository_data_to_json(
                response.json(),
                {'repo_id': repo_id}
            )}
        else:
            self.logger.error('ZenHub API: ' + response.json().get('message', ''))
            response.raise_for_status()

    def test(self):
        return self.connection.test()
