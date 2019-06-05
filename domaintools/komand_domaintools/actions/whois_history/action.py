import komand
from .schema import WhoisHistoryInput, WhoisHistoryOutput
# Custom imports below
from komand_domaintools.util import util


class WhoisHistory(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='whois_history',
                description='Provides a list of historic Whois records for a domain name',
                input=WhoisHistoryInput(),
                output=WhoisHistoryOutput())

    def run(self, params={}):
        query = params.get('domain')
        response = utils.make_request(self.connection.api.whois_history, query)
        return response

    def test(self):
        """TODO: Test action"""
        return {}
