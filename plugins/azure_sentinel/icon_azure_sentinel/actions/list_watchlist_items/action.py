import insightconnect_plugin_runtime
from .schema import ListWatchlistItemsInput, ListWatchlistItemsOutput, Input, Output, Component

from icon_azure_sentinel.util.tools import return_non_empty, map_output


class ListWatchlistItems(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_watchlist_items",
            description=Component.DESCRIPTION,
            input=ListWatchlistItemsInput(),
            output=ListWatchlistItemsOutput(),
        )

    def run(self, params={}):
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        watchlist_alias = params.get(Input.WATCHLISTALIAS)

        data_dict = self.connection.api_client.list_watchlist_items(
            resource_group_name, workspace_name, subscription_id, watchlist_alias
        )
        data_dict = map_output(data_dict)
        data_dict = return_non_empty(data_dict)
        return {Output.WATCHLISTITEMS: data_dict.get("value")}
