import komand
from .schema import SearchByNameInput, SearchByNameOutput
# Custom imports below


class SearchByName(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_by_name',
                description='Search hosts by name',
                input=SearchByNameInput(),
                output=SearchByNameOutput())

    def run(self, params={}):
        name_pattern = params.get('name_pattern')
        hosts = self.connection.infoblox_connection.search_by_name(
            name_pattern
        )
        return {'result': hosts}

    def test(self):
        return {
            'result': [{
                '_ref': (
                    'record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmNvbS5pbmZvLmFieA:'
                    'abx.info.com/default'
                ),
                'ipv4addrs': [{
                    '_ref': (
                        'record:host_ipv4addr/ZG5zLmhvc3RfYWRkcmVzcyQuX2RlZmF1'
                        'bHQuY29tLmluZm8uYWJ4LjEwLjEwLjEwLjUyLg:10.10.10.52/'
                        'abx.info.com/default'
                    ),
                    'configure_for_dhcp': False,
                    'host': 'abx.info.com',
                    'ipv4addr': '10.10.10.52'
                }],
                'name': 'abx.info.com',
                'view': 'default'
            }, {
                '_ref': (
                    'record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmNvbS5pbmZvLnRlc3Qz:'
                    'test3.info.com/default'
                ),
                'ipv4addrs': [{
                    '_ref': (
                        'record:host_ipv4addr/ZG5zLmhvc3RfYWRkcmVzcyQuX2RlZmF1'
                        'bHQuY29tLmluZm8udGVzdDMuMTAuMTAuMTAuMjIu:10.10.10.22/'
                        'test3.info.com/default'
                    ),
                    'configure_for_dhcp': True,
                    'host': 'test3.info.com',
                    'ipv4addr': '10.10.10.22',
                    'mac': '11:22:33:11:22:33'
                }],
                'name': 'test3.info.com',
                'view': 'default'
            }]
        }
