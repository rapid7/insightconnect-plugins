import komand
from .schema import SearchCellsInput, SearchCellsOutput
# Custom imports below
from komand_wigle.util.utils import clear_empty_values


class SearchCells(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_cells',
                description='Query the WiGLE cell database for paginated results based on multiple criteria',
                input=SearchCellsInput(),
                output=SearchCellsOutput())

    def run(self, params={}):
        self.logger.info('SearchCells: Sending a query to the server ...')
        p = clear_empty_values(params)
        response = self.connection.call_api('get', 'cell/search', params=p)

        return {
            k: response[k] for k in (
                'totalResults', 'search_after', 'first', 'last',
                'resultCount', 'results'
            ) if k in response
        }

    def test(self):
        return {
          'totalResults': 999,
          'search_after': 20,
          'first': 1,
          'last': 2,
          'resultCount': 2,
          'results': [
            {
              'trilat': 48.01654816,
              'trilong': 37.82863617,
              'ssid': 'MTS UKR',
              'qos': 2,
              'transid': '20120817-00000',
              'firsttime': '2012-08-17T08:00:00.000Z',
              'lasttime': '2012-11-24T07:00:00.000Z',
              'lastupdt': '2018-03-28T22:00:00.000Z',
              'city': 'Донецьк',
              'region': 'Донецька область',
              'country': 'UA',
              'id': '25501_60827_12832',
              'attributes': 'GPRS;ua',
              'gentype': 'GSM'
            },
            {
              'trilat': 37.49578476,
              'trilong': 13.44348812,
              'qos': 0,
              'transid': '20150424-00000',
              'firsttime': '2015-04-24T20:00:00.000Z',
              'lasttime': '2015-04-24T20:00:00.000Z',
              'lastupdt': '2018-03-28T22:00:00.000Z',
              'housenumber': '',
              'road': 'Strada Statale Corleonese Agrigentina',
              'city': '',
              'region': 'SIC',
              'country': 'IT',
              'id': '22288_45091_38424959',
              'attributes': 'UMTS;it',
              'gentype': 'GSM'
            }
          ]
        }
