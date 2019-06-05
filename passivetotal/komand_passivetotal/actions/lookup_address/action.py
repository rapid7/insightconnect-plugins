import komand
from .schema import LookupAddressInput, LookupAddressOutput
# Custom imports below
from komand_passivetotal.util import util


class LookupAddress(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='lookup_address',
                description='Lookup IP address',
                input=LookupAddressInput(),
                output=LookupAddressOutput())

    def run(self, params={}):
        address = params['address']
        self.logger.info('Lookup Address: %s', address)
        results = self.connection.enrichment.get_bulk_enrichment(query=[address])
        if results and 'results' in results:
            self.logger.debug('Returned: %s', results)
            record = results['results'].get(address)
            return {'address_record': util.get_address(record or {}), 'found': not not record}

        return {'found': False}

    def test(self):
        # TODO: Implement test function
        return {}
