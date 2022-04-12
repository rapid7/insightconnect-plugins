import insightconnect_plugin_runtime
from .schema import CreateOrUpdateSavedSearchInput, CreateOrUpdateSavedSearchOutput, Input, Component

# Custom imports below


class CreateOrUpdateSavedSearch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_or_update_saved_search",
            description=Component.DESCRIPTION,
            input=CreateOrUpdateSavedSearchInput(),
            output=CreateOrUpdateSavedSearchOutput(),
        )

    def run(self, params={}):
        subscription_id = params.get(Input.SUBSCRIPTION_ID)
        resource_group_name = params.get(Input.RESOURCE_GROUP_NAME)
        workspace_name = params.get(Input.WORKSPACE_NAME)
        saved_search_name = params.get(Input.SAVED_SEARCH_NAME)
        properties = params.get(Input.PROPERTIES)
        return self.connection.client.create_or_update_saved_search(
            subscription_id, resource_group_name, workspace_name, saved_search_name, properties
        )
