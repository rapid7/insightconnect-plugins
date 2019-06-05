import komand
from .schema import DomainSearchInput, DomainSearchOutput
# Custom imports below
from komand_domaintools.util import util


class DomainSearch(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='domain_search',
                description='Searches for domain names that match your specific search string',
                input=DomainSearchInput(),
                output=DomainSearchOutput())

    def run(self, params={}):
        params = komand.helper.clean_dict(params)
        response = utils.make_request(self.connection.api.domain_search, **params)
        return response

    def test(self):
        """TODO: Test action"""
        return {}
