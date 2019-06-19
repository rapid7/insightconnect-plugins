import komand
from .schema import GetCountryStatisticsInput, GetCountryStatisticsOutput
# Custom imports below


class GetCountryStatistics(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_country_statistics',
                description='Get statistics organized by country',
                input=GetCountryStatisticsInput(),
                output=GetCountryStatisticsOutput())

    def run(self, params={}):
        self.logger.info('GetCountryStatistics: Fetching countries statistics ...')
        response = self.connection.call_api('get', 'stats/countries')
        return response

    def test(self):
        return {
          "countries": [
            {
              "country": "US",
              "count": 203188123
            },
            {
              "country": "DE",
              "count": 34100489
            },
            {
              "country": "NL",
              "count": 24067503
            },
            {
              "country": "CA",
              "count": 21483456
            },
            {
              "country": "JP",
              "count": 12013736
            }
          ]
        }
