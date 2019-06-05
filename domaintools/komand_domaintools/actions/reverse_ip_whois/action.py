import komand
from .schema import ReverseIpWhoisInput, ReverseIpWhoisOutput
# Custom imports below
from komand_domaintools.util import util


class ReverseIpWhois(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='reverse_ip_whois',
                description='Provides a list of IP network ranges with Whois records that match a specific query',
                input=ReverseIpWhoisInput(),
                output=ReverseIpWhoisOutput())

    def run(self, params={}):
        params = komand.helper.clean_dict(params)
        response = utils.make_request(self.connection.api.reverse_ip_whois, **params)
        return response

    def test(self):
        """TODO: Test action"""
        return {}
