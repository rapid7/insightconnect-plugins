import komand
from .schema import SearchInput, SearchOutput
# Custom imports below
import json


class Search(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search',
                description='Run a query',
                input=SearchInput(),
                output=SearchOutput())

    def run(self, params={}):
        """Run action"""
        result = self.connection.client.jobs.oneshot(
                params.get('query'), count=params.get('count'), output_mode='json')
        results = json.loads(result.readall())

        count = 0
        if 'results' in results:
            count = len(results['results'])

        return {'result': results, 'count': count}

    def test(self):
        return {}
