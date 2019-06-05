import komand
from .schema import SpfInput, SpfOutput
# Custom imports below
from komand_mxtoolbox_dns.util import utils


class Spf(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='spf',
                description='Check SPF records on a domain',
                input=SpfInput(),
                output=SpfOutput())

    def run(self, params={}):
        base_url = self.connection.server
        token = self.connection.token
        host = params.get("hostname")
        request_url = base_url + "lookup/spf/" + host
        return utils.query_api(request_url, token)

    def test(self):
        base_url = self.connection.server
        token = self.connection.token
        request_url = base_url + "lookup/spf/example.com"
        return utils.test_api(request_url, token)
