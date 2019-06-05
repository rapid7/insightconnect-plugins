import komand
from .schema import (
    SearchForEndpointHostnameUsagesInput, SearchForEndpointHostnameUsagesOutput
)
# Custom imports below


class SearchForEndpointHostnameUsages(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_for_endpoint_hostname_usages',
                description='Finds usages of an endpoint hostname',
                input=SearchForEndpointHostnameUsagesInput(),
                output=SearchForEndpointHostnameUsagesOutput())

    def run(self, params={}):
        endpoint_hostname = params.get('endpoint_hostname')
        max_results = params.get('max_results', 100)

        results = self.connection.api.search_for_endpoint_hostname_usages(
            endpoint_hostname, max_results
        )

        return {'results': results}
