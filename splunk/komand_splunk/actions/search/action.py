import komand
from .schema import SearchInput, SearchOutput, Input, Output, Component
# Custom imports below
import json


class Search(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search',
                description=Component.DESCRIPTION,
                input=SearchInput(),
                output=SearchOutput())

    def run(self, params={}):
        """Run action"""
        result = self.connection.client.jobs.oneshot(
                params.get(Input.QUERY), count=params.get(Input.COUNT), output_mode="json")
        results = json.loads(result.readall())

        count = 0
        if "results" in results:
            count = len(results["results"])

        return {Output.RESULT: results, Output.COUNT: count}
