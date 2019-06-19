import komand
from .schema import GetUserStatisticsInput, GetUserStatisticsOutput
# Custom imports below


class GetUserStatistics(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_user_statistics',
                description='Get statistics and badge image for the authenticated user',
                input=GetUserStatisticsInput(),
                output=GetUserStatisticsOutput())

    def run(self, params={}):
        self.logger.info('GetUserStatistics: Fetching user statistics ...')
        response = self.connection.call_api('get', 'stats/user')
        return response

    def test(self):
        return {
          "imageBadgeUrl": "/bi/ImEIm375GH87487BSgxYew.png",
          "statistics": {
            "rank": 0,
            "monthRank": 0,
            "userName": "test_user",
            "discoveredWiFiGPS": 0,
            "discoveredWiFiGPSPercent": 0,
            "discoveredWiFi": 0,
            "discoveredCellGPS": 0,
            "discoveredCell": 0,
            "eventMonthCount": 0,
            "eventPrevMonthCount": 0,
            "prevRank": 0,
            "prevMonthRank": 0,
            "totalWiFiLocations": 0,
            "self": True
          },
          "rank": 0,
          "monthRank": 0,
          "user": "test_user",
          "message": "No stats for user. Upload data to participate."
        }
