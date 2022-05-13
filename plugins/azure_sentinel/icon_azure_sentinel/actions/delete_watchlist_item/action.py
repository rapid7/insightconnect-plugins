import insightconnect_plugin_runtime
from .schema import DeleteWatchlistItemInput, DeleteWatchlistItemOutput, Input, Output, Component

from icon_azure_sentinel.util.tools import return_non_empty, map_output


class DeleteWatchlistItem(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_watchlist_item",
            description=Component.DESCRIPTION,
            input=DeleteWatchlistItemInput(),
            output=DeleteWatchlistItemOutput(),
        )

    def run(self, params={}):
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        watchlist_alias = params.get(Input.WATCHLISTALIAS)
        watchlist_item_id = params.get(Input.WATCHLISTITEMID)

        self.connection.api_client.delete_watchlist_items(
            resource_group_name, workspace_name, subscription_id, watchlist_alias, watchlist_item_id
        )
        return {Output.MESSAGE: f"Watchlist item name: {watchlist_item_id} deleted"}
