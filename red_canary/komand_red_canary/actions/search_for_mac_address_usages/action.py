import komand
from .schema import (
    SearchForMacAddressUsagesInput, SearchForMacAddressUsagesOutput
)
# Custom imports below


class SearchForMacAddressUsages(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_for_mac_address_usages',
                description='Finds usages of a MAC address',
                input=SearchForMacAddressUsagesInput(),
                output=SearchForMacAddressUsagesOutput())

    def run(self, params={}):
        mac_address = params.get('mac_address')
        max_results = params.get('max_results', 100)
        results = self.connection.api.search_for_mac_address_usages(
            mac_address, max_results
        )
        return {'results': results}
