import komand
from .schema import ListSavedSearchesInput, ListSavedSearchesOutput, Input, Output, Component
# Custom imports below
import json


class ListSavedSearches(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_saved_searches',
                description=Component.DESCRIPTION,
                input=ListSavedSearchesInput(),
                output=ListSavedSearchesOutput())

    def run(self, params={}):
        saved_searches = self.connection.client.saved_searches.list()

        saved_searches_json = list()

        # Do all this nonsense to get our results into json array
        for saved_search in saved_searches:
            # Create JSON string from SavedSearch object
            new_json = json.dumps(saved_search, default=lambda o: o.__dict__, sort_keys=True, indent=4)

            # Append JSON-serializable object to list
            saved_searches_json.append(json.loads(new_json))

        return {Output.SAVED_SEARCHES: saved_searches_json}
