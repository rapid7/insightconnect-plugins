import komand
from .schema import GetNetworkDetailsInput, GetNetworkDetailsOutput
# Custom imports below
from komand_wigle.util.utils import clear_empty_values


class GetNetworkDetails(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_network_details',
                description='Get details and observation records for a single network',
                input=GetNetworkDetailsInput(),
                output=GetNetworkDetailsOutput())

    def run(self, params={}):
        self.logger.info('GetNetworkDetails: Fetching network details ...')
        p = clear_empty_values(params)
        response = self.connection.call_api(
            'get', 'network/detail', params=p
        )
        return response

    def test(self):
        return {
          "cdma": False,
          "gsm": False,
          "wifi": False,
          "addresses": [
            {
              "address": {
                "country": "日本",
                "country_code": "jp"
              },
              "lat": 36.5748441,
              "lon": 139.2394179,
              "importance": 0.90670922399871,
              "place_id": 174823796,
              "licence": "Data © OpenStreetMap contributors, ODbL 1.0. http://www.openstreetmap.org/copyright",
              "osm_type": "relation",
              "display_name": "日本",
              "boundingbox": [
                20.2145811,
                45.7112046,
                122.7141754,
                154.205541
              ]
            }
          ],
          "results": [
            {
              "trilat": 34.73895264,
              "trilong": 137.40457153,
              "ssid": "1B701C0F5DABA53F414E1A9D367131E9",
              "qos": 2,
              "transid": "20150725-00538",
              "firsttime": "2015-07-26T19:58:22.000Z",
              "lasttime": "2016-03-29T06:15:31.000Z",
              "lastupdt": "2018-08-29T08:32:52.000Z",
              "netid": "00:1D:73:0B:4F:B0",
              "type": "infra",
              "comment": "Appended by test_user on 2018-08-29 01:05:54:\n\nA comment\n\nAppended by test_user on 2018-08-29 01:32:40:\n\nAcomment\n\nAppended by test_user on 2018-08-29 01:32:52:\n\nA comment",
              "wep": "W",
              "channel": 11,
              "bcninterval": 0,
              "freenet": "?",
              "dhcp": "?",
              "paynet": "?",
              "locationData": [
                {
                  "alt": 74,
                  "accuracy": 4,
                  "lastupdt": "2015-07-26T04:05:07.000Z",
                  "latitude": 34.7383728,
                  "longitude": 137.40545654,
                  "month": "201507",
                  "ssid": "1B701C0F5DABA53F414E1A9D367131E9",
                  "time": "2015-07-26T19:58:22.000Z",
                  "signal": -80,
                  "name": "Clever name",
                  "netId": "126484172720",
                  "noise": 0,
                  "snr": 0,
                  "wep": "W",
                  "encryptionValue": "WPA"
                }
              ],
              "encryption": "wpa"
            }
          ]
        }
