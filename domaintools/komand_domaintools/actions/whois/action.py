import komand
from .schema import WhoisInput, WhoisOutput
# Custom imports below
from komand_domaintools.util import util


class Whois(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='whois',
                description='Provides the ownership record for a domain name or IP address with basic registration details',
                input=WhoisInput(),
                output=WhoisOutput())

    def run(self, params={}):
        query = params.get('query')
        response = utils.make_request(self.connection.api.whois, query)
        return response

    def test(self):
        """TODO: Test action"""
        return {}
