import komand
from .schema import SimpleSearchInput, SimpleSearchOutput
# Custom imports below
from komand.helper import clean


class SimpleSearch(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='simple_search',
                description='Execute a simple search for a string',
                input=SimpleSearchInput(),
                output=SimpleSearchOutput())

    def run(self, params={}):
        text = params.get('text')
        results = self.connection.api.simple_search(text)

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
