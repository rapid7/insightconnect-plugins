import komand
from .schema import GetUserStandingsInput, GetUserStandingsOutput
# Custom imports below
from komand_wigle.util.utils import clear_empty_values


class GetUserStandings(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_user_standings',
                description='Get user standings',
                input=GetUserStandingsInput(),
                output=GetUserStandingsOutput())

    def run(self, params={}):
        params = clear_empty_values(params)
        sort = params.get('sort', None)
        pagestart = params.get('pagestart', None)
        pageend = params.get('pageend', None)
        self.logger.info('GetUserStandings: Fetching user standings ...')
        response = self.connection.call_api(
            'get', 'stats/standings', params={
                'sort': sort, 'pagestart': pagestart, 'pageend': pageend
            }
        )
        return response

    def test(self):
        return {
          "eventView": False,
          "myUsername": "",
          "pageStart": 0,
          "pageEnd": 100,
          "totalUsers": 37023,
          "sortBy": "discovered",
          "results": [
            {
              "rank": 1,
              "monthRank": 0,
              "userName": "anonymous",
              "discoveredWiFiGPS": 36903238,
              "discoveredWiFiGPSPercent": 7.90782,
              "discoveredWiFi": 62723348,
              "discoveredCellGPS": 909784,
              "discoveredCell": 1302131,
              "eventMonthCount": 538224,
              "eventPrevMonthCount": 508524,
              "prevRank": 1,
              "prevMonthRank": 1,
              "totalWiFiLocations": 302954340,
              "first": "20011003-00001",
              "last": "20180829-00227",
              "self": False
            },
            {
              "rank": 2,
              "monthRank": 0,
              "userName": "ccie4526",
              "discoveredWiFiGPS": 12115146,
              "discoveredWiFiGPSPercent": 2.5961,
              "discoveredWiFi": 13522673,
              "discoveredCellGPS": 2155,
              "discoveredCell": 3543,
              "eventMonthCount": 113020,
              "eventPrevMonthCount": 51333,
              "prevRank": 2,
              "prevMonthRank": 15,
              "totalWiFiLocations": 171386632,
              "first": "20030127-00018",
              "last": "20180828-00846",
              "self": False
            }
          ]
        }
