import insightconnect_plugin_runtime
from .schema import DeleteSavedSearchInput, DeleteSavedSearchOutput, Input, Output, Component

# Custom imports below


class DeleteSavedSearch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_saved_search",
            description=Component.DESCRIPTION,
            input=DeleteSavedSearchInput(),
            output=DeleteSavedSearchOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        saved_search_name = params.get(Input.SAVED_SEARCH_NAME)
        # END INPUT BINDING - DO NOT REMOVE

        try:
            self.connection.client.saved_searches.delete(saved_search_name)
        except KeyError as error:
            self.logger.error(error)
            return {"success": False}

        # Do we want to rely on an exception being the only way of knowing if it was successful?
        # We can always do a query of available saved searches to verify, but it might be overkill.
        self.logger.info(f"Deleted saved search {saved_search_name}")
        return {Output.SUCCESS: True}
