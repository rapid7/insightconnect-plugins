import komand
from .schema import DnsInput, DnsOutput
# Custom imports below
from komand_mxtoolbox_dns.util import utils


class Dns(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='dns',
                description='Run a DNS query',
                input=DnsInput(),
                output=DnsOutput())

    def run(self, params={}):
        base_url = self.connection.server
        token = self.connection.token
        host = params.get("hostname")
        request_url = base_url + "lookup/dns/" + host
        return utils.query_api(request_url, token)

    def test(self):
        base_url = self.connection.server
        token = self.connection.token
        request_url = base_url + "lookup/dns/example.com"
        return utils.test_api(request_url, token)
