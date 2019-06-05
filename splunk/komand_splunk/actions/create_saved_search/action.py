import komand
from .schema import CreateSavedSearchInput, CreateSavedSearchOutput
# Custom imports below
import json


class CreateSavedSearch(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_saved_search',
                description='Creates a saved search',
                input=CreateSavedSearchInput(),
                output=CreateSavedSearchOutput())

    def run(self, params={}):
        optional_parameters = params.get("properties")
        query = params.get("query")
        saved_search_name = params.get("saved_search_name")

        try:
            new_saved_search = self.connection.client.saved_searches.create(saved_search_name, query, **optional_parameters)
        except:
            self.logger.error("Unable to create saved search")

        self.logger.info("Created new saved search: %s" % new_saved_search.name)

        new_saved_search_json = json.loads(
            json.dumps(new_saved_search, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        )

        return {"saved_search": new_saved_search_json}

    def test(self):
        return {}
