import komand
from .schema import LookupAddressesInput, LookupAddressesOutput
# Custom imports below
from komand_passivetotal.util import util


class LookupAddresses(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='lookup_addresses',
                description='Lookup IP addresses',
                input=LookupAddressesInput(),
                output=LookupAddressesOutput())

    def run(self, params={}):
        addresses = params['addresses'] or []
        self.logger.info('Lookup Address: %s', addresses)
        results = self.connection.enrichment.get_bulk_enrichment(query=addresses)
        self.logger.debug('Returned: %s', results)
        records = []
        found = []
        for addr in addresses:
            record = results['results'].get(addr)
            if record:
                found.append(addr)
                records.append(util.get_address(record or {}))

        return {'address_records': records, 'found_records': found}

    def test(self):
        # TODO: Implement test function
        return {}
