import komand
from .schema import MxInput, MxOutput
# Custom imports below
from komand_mxtoolbox_dns.util import utils


class Mx(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='mx',
                description='DNS MX records for domain',
                input=MxInput(),
                output=MxOutput())

    def run(self, params={}):
        base_url = self.connection.server
        token = self.connection.token
        host = params.get("hostname")
        request_url = base_url + "lookup/mx/" + host
        return utils.query_api(request_url, token)

    def test(self):
        base_url = self.connection.server
        token = self.connection.token
        request_url = base_url + "lookup/mx/example.com"
        return utils.test_api(request_url, token)
