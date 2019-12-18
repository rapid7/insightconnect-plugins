import komand
from .schema import SearchByIpInput, SearchByIpOutput
# Custom imports below


class SearchByIp(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_by_ip',
                description='Search hosts by IP address',
                input=SearchByIpInput(),
                output=SearchByIpOutput())

    def run(self, params={}):
        ip = params.get('ip')
        objects = self.connection.infoblox_connection.search_by_ip(ip)
        result = []
        for o in objects:
            result.extend(o['objects'])
        return {'result': result}

    def test(self):
        return {
            'result': [(
                'fixedaddress/ZG5zLmZpeGVkX2FkZHJlc3MkMTAuMTAuMTAuNS4wLi4:'
                '10.10.10.5/default'
            )]
        }
