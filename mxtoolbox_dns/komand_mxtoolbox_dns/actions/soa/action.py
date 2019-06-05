import komand
from .schema import SoaInput, SoaOutput
# Custom imports below
from komand_mxtoolbox_dns.util import utils


class Soa(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='soa',
                description='Get Start of Authority record for a domain',
                input=SoaInput(),
                output=SoaOutput())

    def run(self, params={}):
        base_url = self.connection.server
        token = self.connection.token
        host = params.get("hostname")
        request_url = base_url + "lookup/soa/" + host
        return utils.query_api(request_url, token)

    def test(self):
        base_url = self.connection.server
        token = self.connection.token
        request_url = base_url + "lookup/soa/example.com"
        return utils.test_api(request_url, token)
