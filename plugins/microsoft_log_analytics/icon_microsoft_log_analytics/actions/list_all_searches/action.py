import insightconnect_plugin_runtime
from .schema import ListAllSearchesInput, ListAllSearchesOutput, Input, Output, Component

# Custom imports below


class ListAllSearches(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_all_searches",
            description=Component.DESCRIPTION,
            input=ListAllSearchesInput(),
            output=ListAllSearchesOutput(),
        )

    def run(self, params={}):
        subscription_id = params.get(Input.SUBSCRIPTION_ID)
        resource_group_name = params.get(Input.RESOURCE_GROUP_NAME)
        workspace_name = params.get(Input.WORKSPACE_NAME)
        response = self.connection.client.list_all_searches(subscription_id, resource_group_name, workspace_name)
        return {Output.SAVED_SEARCHES: response}
