import komand
from .schema import TxtInput, TxtOutput
# Custom imports below
from komand_mxtoolbox_dns.util import utils


class Txt(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='txt',
                description='Check TXT records on a domain',
                input=TxtInput(),
                output=TxtOutput())

    def run(self, params={}):
        base_url = self.connection.server
        token = self.connection.token
        host = params.get("hostname")
        request_url = base_url + "lookup/txt/" + host
        return utils.query_api(request_url, token)

    def test(self):
        base_url = self.connection.server
        token = self.connection.token
        request_url = base_url + "lookup/txt/example.com"
        return utils.test_api(request_url, token)
