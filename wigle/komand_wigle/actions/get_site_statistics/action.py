import komand
from .schema import GetSiteStatisticsInput, GetSiteStatisticsOutput
# Custom imports below


class GetSiteStatistics(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_site_statistics',
                description='Get a map of short-named statistics used in providing site-wide information',
                input=GetSiteStatisticsInput(),
                output=GetSiteStatisticsOutput())

    def run(self, params={}):
        self.logger.info('GetSiteStatistics: Fetching site statistics ...')
        response = self.connection.call_api('get', 'stats/site')
        return {'statistics': response}

    def test(self):
        return {
          "statistics": {
            "netwpa2": 297903981,
            "netwpa3": 1,
            "gentotal": 10004950,
            "netnowep": 20677193,
            "dfltssid": 13104735,
            "dfltwpkn": 0,
            "trans2da": 961,
            "netwpa": 29079784,
            "trans1da": 1064,
            "nettotal": 471930775,
            "nettoday": 52442,
            "netwep?": 92493113,
            "loctotal": 6730687824,
            "netwep": 32294188,
            "netwwwd3": 221378,
            "transtot": 2341606,
            "waitQueue": 0,
            "size": 24,
            "dfltnowp": 0,
            "genloc": 9949211,
            "netlocdy": 52193,
            "netloc": 466666310,
            "transtdy": 224,
            "userstot": 216690,
            "netlocd2": 292860
          }
        }
