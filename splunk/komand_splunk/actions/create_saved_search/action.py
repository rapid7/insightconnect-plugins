import komand
from .schema import CreateSavedSearchInput, CreateSavedSearchOutput, Input, Output, Component
# Custom imports below
import json
from komand.exceptions import PluginException


class CreateSavedSearch(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_saved_search',
                description=Component.DESCRIPTION,
                input=CreateSavedSearchInput(),
                output=CreateSavedSearchOutput())

    def run(self, params={}):
        optional_parameters = params.get(Input.PROPERTIES)
        query = params.get(Input.QUERY)
        saved_search_name = params.get(Input.SAVED_SEARCH_NAME)

        try:
            new_saved_search = self.connection.client.saved_searches.create(saved_search_name,
                                                                            query,
                                                                            **optional_parameters)
        except Exception as e:
            raise PluginException(cause="Unable to create saved search!",
                                  assistance="Ensure your properties and query are valid.",
                                  data=e) from e

        self.logger.info("Created new saved search: %s" % new_saved_search.name)

        new_saved_search_json = json.loads(
            json.dumps(new_saved_search, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        )

        return {Output.SAVED_SEARCH: new_saved_search_json}
