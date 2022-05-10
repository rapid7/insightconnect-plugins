import insightconnect_plugin_runtime
from .schema import ListWatchlistsInput, ListWatchlistsOutput, Input, Output, Component

# Custom imports below


class ListWatchlists(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_watchlists",
            description=Component.DESCRIPTION,
            input=ListWatchlistsInput(),
            output=ListWatchlistsOutput(),
        )

    def run(self, params={}):
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)
        watchlists = self.connection.api_client.list_watchlists(resource_group_name, workspace_name, subscription_id)
        return {Output.WATCHLISTS: watchlists}
