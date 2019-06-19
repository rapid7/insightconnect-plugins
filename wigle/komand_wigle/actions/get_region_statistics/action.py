import komand
from .schema import GetRegionStatisticsInput, GetRegionStatisticsOutput
# Custom imports below


class GetRegionStatistics(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_region_statistics',
                description='Get statistics for a specified country, organized by region',
                input=GetRegionStatisticsInput(),
                output=GetRegionStatisticsOutput())

    def run(self, params={}):
        country = params.get('country', 'us')
        self.logger.info('GetRegionStatistics: Fetching region statistics ...')
        response = self.connection.call_api(
            'get', 'stats/regions', params={'country': country}
        )
        return response

    def test(self):
        return {
          "country": "jp",
          "regions": [
            {
              "region": "東京都",
              "count": 5907792
            },
            {
              "region": "神奈川県",
              "count": 750393
            }
          ],
          "encryption": [
            {
              "wep": "2",
              "count": 7160339
            },
            {
              "wep": "Y",
              "count": 1941846
            }
          ],
          "postalCode": [
            {
              "postalCode": "052-201-4814",
              "count": 80525
            },
            {
              "postalCode": "460-8688",
              "count": 79119
            }
          ]
        }
