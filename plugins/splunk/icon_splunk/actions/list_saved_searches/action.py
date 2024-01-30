import insightconnect_plugin_runtime
from .schema import ListSavedSearchesInput, ListSavedSearchesOutput, Input, Output, Component

# Custom imports below
import json


class ListSavedSearches(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_saved_searches",
            description=Component.DESCRIPTION,
            input=ListSavedSearchesInput(),
            output=ListSavedSearchesOutput(),
        )

    def run(self, params={}):
        # pylint: disable=unused-argument
        saved_searches_json = []
        for saved_search in self.connection.client.saved_searches.list():
            # Create JSON string from SavedSearch object
            new_json = json.dumps(saved_search, default=lambda object_: object_.__dict__, sort_keys=True, indent=4)

            # Append JSON-serializable object to list
            saved_searches_json.append(json.loads(new_json))
        return {Output.SAVED_SEARCHES: saved_searches_json}
