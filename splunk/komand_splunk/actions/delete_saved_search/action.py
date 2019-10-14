import komand
from .schema import DeleteSavedSearchInput, DeleteSavedSearchOutput, Input, Output, Component
# Custom imports below


class DeleteSavedSearch(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_saved_search',
                description=Component.DESCRIPTION,
                input=DeleteSavedSearchInput(),
                output=DeleteSavedSearchOutput())

    def run(self, params={}):
        saved_search_name = params.get(Input.SAVED_SEARCH_NAME)

        try:
            self.connection.client.saved_searches.delete(saved_search_name)
        except KeyError as error:
            self.logger.error(error)
            return {"success": False}

        # Do we want to rely on an exception being the only way of knowing if it was successful?
        # We can always do a query of available saved searches to verify, but it might be overkill.
        self.logger.info("Deleted saved search %s" % saved_search_name)
        return {Output.SUCCESS: True}
