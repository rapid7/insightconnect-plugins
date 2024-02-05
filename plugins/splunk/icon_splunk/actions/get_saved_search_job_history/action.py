import insightconnect_plugin_runtime
from .schema import (
    GetSavedSearchJobHistoryInput,
    GetSavedSearchJobHistoryOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
import json
from insightconnect_plugin_runtime.exceptions import PluginException
from json import JSONDecodeError


class GetSavedSearchJobHistory(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_saved_search_job_history",
            description=Component.DESCRIPTION,
            input=GetSavedSearchJobHistoryInput(),
            output=GetSavedSearchJobHistoryOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        saved_search_name = params.get(Input.SAVED_SEARCH_NAME)
        # END INPUT BINDING - DO NOT REMOVE

        try:
            saved_search = self.connection.client.saved_searches[saved_search_name]
            history = saved_search.history()  # Returns a list of Job objects
        except KeyError as error:
            raise PluginException(
                cause="The specified saved search was not found.",
                assistance=f"Ensure the saved search '{saved_search_name}' exists.",
                data=error,
            )

        try:
            history_json = json.loads(
                json.dumps(history, default=lambda objects_: objects_.__dict__, sort_keys=True, indent=4)
            )
        except JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)
        return {Output.JOB_HISTORY: history_json}
