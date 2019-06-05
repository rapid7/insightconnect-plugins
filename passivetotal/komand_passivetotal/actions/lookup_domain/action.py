import komand
from .schema import LookupDomainInput, LookupDomainOutput
# Custom imports below
from komand_passivetotal.util import util


class LookupDomain(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='lookup_domain',
                description='Lookup Domain',
                input=LookupDomainInput(),
                output=LookupDomainOutput())

    def run(self, params={}):
        domain = params['domain']
        self.logger.info('Lookup domain: %s', domain)
        results = self.connection.enrichment.get_bulk_enrichment(query=[domain])
        self.logger.debug('Returned: %s', results)
        record = results['results'].get(domain)
        return {'domain_record': util.get_domain(record or {}), 'found': not not record}

    def test(self):
        # TODO: Implement test function
        return {}
