import komand
from .schema import GetEpicDataInput, GetEpicDataOutput
# Custom imports below
import json
from komand_zenhub.util import helper


class GetEpicData(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_epic_data',
                description='Get the ZenHub Data for a ZenHub Epic',
                input=GetEpicDataInput(),
                output=GetEpicDataOutput())

    def run(self, params={}):
        response = self.connection.request(
            'GET', ('repositories', params.get('repo_id'),
                    'epics', params.get('epic_id'))
        )
        if response.ok:
            return {'data': helper.epic_data_to_json(response.json())}
        else:
            self.logger.error('ZenHub API: ' + response.json().get('message', ''))
            response.raise_for_status()

    def test(self):
        return self.connection.test()
