#This action requires an account. It cannot use example.com because input must be in
#the form of an IP address
import komand
from .schema import PtrInput, PtrOutput
# Custom imports below
from komand_mxtoolbox_dns.util import utils


class Ptr(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='ptr',
                description='DNS PTR record for host name',
                input=PtrInput(),
                output=PtrOutput())

    def run(self, params={}):
        base_url = self.connection.server
        token = self.connection.token
        host = params.get("ip_address")
        request_url = base_url + "lookup/ptr/" + host
        return utils.query_api(request_url, token)

    def test(self):
        base_url = self.connection.server
        token = self.connection.token
        request_url = base_url + "lookup/ptr/example.com"
        return utils.test_api(request_url, token)
