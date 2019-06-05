import komand
from .schema import ParsedWhoisInput, ParsedWhoisOutput
# Custom imports below
from komand_domaintools.util import util


class ParsedWhois(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='parsed_whois',
                description='Provides parsed information extracted from the raw Whois record',
                input=ParsedWhoisInput(),
                output=ParsedWhoisOutput())

    def run(self, params={}):
        query = params.get('domain')
        response = utils.make_request(self.connection.api.parsed_whois, query)
        return response

    def test(self):
        """TODO: Test action"""
        return {}
