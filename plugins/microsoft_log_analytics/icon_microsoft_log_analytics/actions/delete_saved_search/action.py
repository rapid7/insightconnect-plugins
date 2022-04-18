import insightconnect_plugin_runtime
from .schema import DeleteSavedSearchInput, DeleteSavedSearchOutput, Input, Output, Component

# Custom imports below
from icon_microsoft_log_analytics.util.tools import Message


class DeleteSavedSearch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_saved_search",
            description=Component.DESCRIPTION,
            input=DeleteSavedSearchInput(),
            output=DeleteSavedSearchOutput(),
        )

    def run(self, params={}):
        subscription_id = params.get(Input.SUBSCRIPTION_ID)
        resource_group_name = params.get(Input.RESOURCE_GROUP_NAME)
        workspace_name = params.get(Input.WORKSPACE_NAME)
        saved_search_name = params.get(Input.SAVED_SEARCH_NAME)
        response = self.connection.client.delete_saved_search(
            subscription_id, resource_group_name, workspace_name, saved_search_name
        )
        return {
            Output.MESSAGE: Message.DELETE_SAVED_SEARCH_MESSAGE.format(saved_search_name),
            Output.DELETED_SAVED_SEARCH: response,
        }
