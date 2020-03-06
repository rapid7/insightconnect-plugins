import komand
from .schema import SearchDbInput, SearchDbOutput, Input, Output
# Custom imports below
from typing import Dict, List
import requests
from komand_rapid7_vulndb.util import utils


class SearchDb(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='search_db',
            description='Search the database to find vulnerabilities and exploits',
            input=SearchDbInput(),
            output=SearchDbOutput())

    def run(self, params={}):
        # Get params
        search = params.get(Input.SEARCH)
        data_base = params.get(Input.DATABASE)

        q = {"query": search}
        q = utils.R7VDB.set_query_db_type(q, data_base)
        data = utils.R7VDB.get_query(q)
        num_of_pages = data['metadata']['total_pages']
        results = utils.R7VDB.paginate_search(q, num_of_pages)
        return {
            Output.RESULTS_FOUND: len(results),
            Output.SEARCH_RESULTS: results,
        }
