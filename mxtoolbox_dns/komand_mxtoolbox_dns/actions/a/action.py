import komand
from .schema import AInput, AOutput
# Custom imports below
from komand_mxtoolbox_dns.util import utils


class A(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='a',
                description='DNS A record IP address for host name',
                input=AInput(),
                output=AOutput())

    def run(self, params={}):
        base_url = self.connection.server
        token = self.connection.token
        host = params.get("hostname")
        request_url = base_url + "lookup/a/" + host
        return utils.query_api(request_url, token)

    def test(self):
        base_url = self.connection.server
        token = self.connection.token
        request_url = base_url + "lookup/a/example.com"
        return utils.test_api(request_url, token)
