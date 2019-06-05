import komand
from .schema import LookupDomainsInput, LookupDomainsOutput
# Custom imports below
from komand_passivetotal.util import util


class LookupDomains(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='lookup_domains',
                description='Lookup Domains',
                input=LookupDomainsInput(),
                output=LookupDomainsOutput())

    def run(self, params={}):
        """TODO: Run action"""
        domains = params['domains'] or []
        self.logger.info('Lookup domain: %s', domains)
        results = self.connection.enrichment.get_bulk_enrichment(query=domains)
        self.logger.debug('Returned: %s', results)
        records = []
        found = []
        for addr in domains:
            record = results['results'].get(addr)
            if record:
                found.append(addr)
                records.append(util.get_domain(record or {}))

        return {'domain_records': records, 'found_records': found}

    def test(self):
        # TODO: Implement test function
        return {}
