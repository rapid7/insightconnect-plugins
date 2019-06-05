import komand
from .schema import AdvancedSearchInput, AdvancedSearchOutput
# Custom imports below
from komand.helper import clean


class AdvancedSearch(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='advanced_search',
                description='Execute a SOQL (Salesforce Object Query Language) query',
                input=AdvancedSearchInput(),
                output=AdvancedSearchOutput())

    def run(self, params={}):
        query = params.get('query')
        results = self.connection.api.advanced_search(query)

        flat_results = []

        for result in results:
            flat_result = {
                'type': result.get('attributes', {}).get('type', ''),
                'url': result.get('attributes', {}).get('url', ''),
                'name': result.get('Name'),
                'id': result.get('Id'),
            }
            flat_result = clean(flat_result)
            flat_results.append(flat_result)

        return {'search_results': flat_results}
