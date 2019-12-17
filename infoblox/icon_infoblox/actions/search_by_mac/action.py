import komand
from .schema import SearchByMacInput, SearchByMacOutput
# Custom imports below


class SearchByMac(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_by_mac',
                description='Search hosts by MAC address',
                input=SearchByMacInput(),
                output=SearchByMacOutput())

    def run(self, params={}):
        mac = params.get('mac')
        result = self.connection.infoblox_connection.search_by_mac(mac)
        return {'result': result}

    def test(self):
        return {
            'result': [{
                '_ref': (
                    'fixedaddress/ZG5zLmZpeGVkX2FkZHJlc3MkMTAuMTAuMTAuMi4wLi4:'
                    '10.10.10.2/default'
                ),
                'ipv4addr': '10.10.10.2',
                'mac': 'aa:bb:cc:11:22:33',
                'network_view': 'default'
            }]
        }
