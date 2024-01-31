import insightconnect_plugin_runtime
from .schema import RunSavedSearchInput, RunSavedSearchOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class RunSavedSearch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="run_saved_search",
            description=Component.DESCRIPTION,
            input=RunSavedSearchInput(),
            output=RunSavedSearchOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        saved_search_name = params.get(Input.SAVED_SEARCH_NAME)
        # END INPUT BINDING - DO NOT REMOVE

        try:
            saved_search = self.connection.client.saved_searches[saved_search_name]
            search_job = saved_search.dispatch()
            job_id = search_job["sid"]  # Search ID
        except KeyError as error:
            raise PluginException(
                cause=f"Saved search {saved_search_name} was not found!",
                assistance="Ensure the saved search exists.",
                data=error,
            )
        return {Output.JOB_ID: job_id}
