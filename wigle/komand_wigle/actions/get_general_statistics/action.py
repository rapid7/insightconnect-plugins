import komand
from .schema import GetGeneralStatisticsInput, GetGeneralStatisticsOutput
# Custom imports below


class GetGeneralStatistics(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_general_statistics',
                description='Get a named map of general statistics',
                input=GetGeneralStatisticsInput(),
                output=GetGeneralStatisticsOutput())

    def run(self, params={}):
        self.logger.info(
            'GetGeneralStatistics: Fetching general statistics ...'
        )
        statistics = self.connection.call_api('get', 'stats/general')
        return {'statistics': statistics}

    def test(self):
        return {
          "statistics":
          {
            "octet": False,
            "netwpa2": 297891746,
            "android": False,
            "netwpa3": 1,
            "gentotal": 10001758,
            "manufacturer": True,
            "netnowep": 20677147,
            "dfltssid": 13104735,
            "dfltwpkn": 0,
            "trans2da": 961,
            "netwpa": 29079578,
            "trans1da": 1064,
            "nettotal": 471916436,
            "nettoday": 38103,
            "netwep?": 92491408,
            "loctotal": 6730417785,
            "netwep": 32294041,
            "ssidStatistics": [
              {
                "name": "xfinitywifi",
                "value": 9533081
              },
              {
                "name": "linksys",
                "value": 3079971
              }
            ],
            "netwwwd3": 221378,
            "manufacturerStatistics": [
              {
                "name": "Cisco Systems, Inc",
                "value": 28263824
              },
              {
                "name": "Netgear",
                "value": 27731830
              }
            ],
            "transtot": 2341560,
            "ieeeManufacturerStatistics": [
              {
                "name": "Cisco Systems, Inc",
                "value": 28454480
              },
              {
                "name": "NETGEAR",
                "value": 27731830
              }
            ],
            "dfltnowp": 0,
            "genloc": 9946019,
            "netlocdy": 37856,
            "netloc": 466651973,
            "transtdy": 178,
            "userstot": 216687,
            "netlocd2": 292860
          }
        }
