import insightconnect_plugin_runtime
from .schema import AdvancedSearchInput, AdvancedSearchOutput, Input, Output, Component

# Custom imports below
from komand_salesforce.util.helpers import clean


class AdvancedSearch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="advanced_search",
            description=Component.DESCRIPTION,
            input=AdvancedSearchInput(),
            output=AdvancedSearchOutput(),
        )

    def run(self, params={}):
        results = self.connection.api.advanced_search(params.get(Input.QUERY))
        flat_results = []

        for result in results:
            flat_results.append(
                {
                    "type": result.get("attributes", {}).get("type", ""),
                    "url": result.get("attributes", {}).get("url", ""),
                    "name": result.get("Name"),
                    "id": result.get("Id"),
                }
            )

        return {Output.SEARCHRESULTS: clean(flat_results)}
