import komand
from .schema import GetGroupStatisticsInput, GetGroupStatisticsOutput
# Custom imports below


class GetGroupStatistics(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_group_statistics',
                description='Get statistics organized by group',
                input=GetGroupStatisticsInput(),
                output=GetGroupStatisticsOutput())

    def run(self, params={}):
        self.logger.info('GetGroupStatistics: Fetching group statistics ...')
        response = self.connection.call_api('get', 'stats/group')
        return response

    def test(self):
        return {
          "groups": [
            {
              "groupId": "20041206-00006",
              "groupName": "Netstumbler Forum users",
              "owner": "g8tk33per",
              "discovered": 21695080,
              "total": 28180457,
              "genDisc": 63853,
              "members": 151,
              "joined": False,
              "groupOwner": False
            },
            {
              "groupId": "20060104-00055",
              "groupName": "The netherlands wireless",
              "owner": "redlin",
              "discovered": 7552591,
              "total": 12977197,
              "genDisc": 116475,
              "members": 23,
              "joined": False,
              "groupOwner": False
            }
          ]
        }
