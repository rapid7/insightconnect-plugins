import insightconnect_plugin_runtime
from .schema import SearchDbInput, SearchDbOutput, Input, Output

# Custom imports below
from komand_rapid7_vulndb.util import extract
from insightconnect_plugin_runtime.helper import clean


class SearchDb(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_db",
            description="Search the database to find vulnerabilities and exploits",
            input=SearchDbInput(),
            output=SearchDbOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        search_for = params.get(Input.SEARCH)
        database = params.get(Input.DATABASE)
        # END INPUT BINDING - DO NOT REMOVE

        responses = extract.Search.get_results(search_for, database)

        results = []
        for response in responses:
            identifier = response.get("identifier")
            if not identifier:
                continue
            dict_response = response.copy()
            dict_response["solutions"] = extract.Content.get(identifier).get("solutions")
            results.append(clean(dict_response))

        return {
            Output.RESULTS_FOUND: len(results) > 0,
            Output.SEARCH_RESULTS: results,
        }
