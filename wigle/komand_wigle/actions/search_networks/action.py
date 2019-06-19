import komand
from .schema import SearchNetworksInput, SearchNetworksOutput
# Custom imports below
from komand_wigle.util.utils import clear_empty_values


class SearchNetworks(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_networks',
                description='Query the WiGLE network database for paginated results based on multiple criteria',
                input=SearchNetworksInput(),
                output=SearchNetworksOutput())

    def run(self, params={}):
        self.logger.info('SearchNetworks: Sending a query to the server ...')
        p = clear_empty_values(params)
        response = self.connection.call_api('get', 'network/search', params=p)

        return {
            k: response[k] for k in (
                'totalResults', 'search_after', 'first', 'last',
                'resultCount', 'results'
            ) if k in response
        }

    def test(self):
        return {
          "totalResults": 471931729,
          "search_after": 377910,
          "first": 1,
          "last": 100,
          "resultCount": 100,
          "results": [
            {
              "trilat": 43.0449028,
              "trilong": 141.29222107,
              "ssid": "0AFEE49737B2C7167C005095768C3228",
              "qos": 0,
              "transid": "20150603-00000",
              "firsttime": "2015-05-31T16:00:00.000Z",
              "lasttime": "2015-06-02T22:00:00.000Z",
              "lastupdt": "2015-06-15T09:00:00.000Z",
              "housenumber": "",
              "road": "裏参道",
              "city": "札幌市",
              "region": "北海道",
              "country": "JP",
              "netid": "00:1D:73:0B:4F:75",
              "type": "infra",
              "wep": "Y",
              "channel": 5,
              "bcninterval": 0,
              "freenet": "?",
              "dhcp": "?",
              "paynet": "?",
              "userfound": False,
              "encryption": "wep"
            },
            {
              "trilat": 34.73895264,
              "trilong": 137.40457153,
              "ssid": "1B701C0F5DABA53F414E1A9D367131E9",
              "qos": 2,
              "transid": "20150725-00000",
              "firsttime": "2015-07-26T12:00:00.000Z",
              "lasttime": "2016-03-28T23:00:00.000Z",
              "lastupdt": "2016-03-28T23:00:00.000Z",
              "housenumber": "",
              "road": "平井牟呂大岩線",
              "city": "豊橋市",
              "region": "愛知県",
              "country": "JP",
              "netid": "00:1D:73:0B:4F:B0",
              "type": "infra",
              "wep": "W",
              "channel": 11,
              "bcninterval": 0,
              "freenet": "?",
              "dhcp": "?",
              "paynet": "?",
              "userfound": False,
              "encryption": "wpa"
            }
          ]
        }
