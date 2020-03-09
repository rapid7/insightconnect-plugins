import komand
from .schema import SearchDbInput, SearchDbOutput, Input, Output
# Custom imports below
from komand_rapid7_vulndb.util import extract


class SearchDb(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='search_db',
            description='Search the database to find vulnerabilities and exploits',
            input=SearchDbInput(),
            output=SearchDbOutput())

    def run(self, params={}):
        # Get params
        search_for = params.get(Input.SEARCH)
        db = params.get(Input.DATABASE)
        results = extract.Search.get_results(search_for, db)
        return {
            Output.RESULTS_FOUND: len(results) > 0,
            Output.SEARCH_RESULTS: results,
        }
