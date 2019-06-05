import komand
from .schema import (
    SearchForIpAddressUsagesInput, SearchForIpAddressUsagesOutput
)
# Custom imports below


class SearchForIpAddressUsages(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_for_ip_address_usages',
                description='Finds usages of an IP address',
                input=SearchForIpAddressUsagesInput(),
                output=SearchForIpAddressUsagesOutput())

    def run(self, params={}):
        ip_address = params.get('ip_address')
        max_results = params.get('max_results', 100)
        results = self.connection.api.search_for_ip_address_usages(
            ip_address, max_results
        )
        return {'results': results}
