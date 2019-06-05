import komand
from .schema import BlacklistInput, BlacklistOutput
# Custom imports below
from komand_mxtoolbox_dns.util import utils


class Blacklist(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='blacklist',
                description='Check IP or host for reputation',
                input=BlacklistInput(),
                output=BlacklistOutput())

    def run(self, params={}):
        base_url = self.connection.server
        token = self.connection.token
        host = params.get("hostname")
        request_url = base_url + "lookup/blacklist/" + host
        return utils.query_api(request_url, token)

    def test(self):
        base_url = self.connection.server
        token = self.connection.token
        request_url = base_url + "lookup/blacklist/example.com"
        return utils.test_api(request_url, token)
