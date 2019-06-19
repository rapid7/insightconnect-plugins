import komand
from .schema import GetNetworkGeocodeInput, GetNetworkGeocodeOutput
# Custom imports below


class GetNetworkGeocode(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_network_geocode',
                description='Get coordinates for an address for use in searching',
                input=GetNetworkGeocodeInput(),
                output=GetNetworkGeocodeOutput())

    def run(self, params={}):
        self.logger.info('GetNetworkGeocode: Fetching data from server ...')
        response = self.connection.call_api(
            'get', 'network/geocode',
            params={'addresscode': params.get('addresscode', None)}
        )
        return response

    def test(self):
        return {
          "results": [
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
          ]
        }
