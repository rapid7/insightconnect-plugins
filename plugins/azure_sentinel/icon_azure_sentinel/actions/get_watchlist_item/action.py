import insightconnect_plugin_runtime
from .schema import GetWatchlistItemInput, GetWatchlistItemOutput, Input, Output, Component

from icon_azure_sentinel.util.tools import return_non_empty, map_output


class GetWatchlistItem(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_watchlist_item",
            description=Component.DESCRIPTION,
            input=GetWatchlistItemInput(),
            output=GetWatchlistItemOutput(),
        )

    def run(self, params={}):
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        watchlist_alias = params.get(Input.WATCHLISTALIAS)
        watchlist_item_id = params.get(Input.WATCHLISTITEMID)

        data_dict = self.connection.api_client.get_watchlist_items(
            resource_group_name, workspace_name, subscription_id, watchlist_alias, watchlist_item_id
        )
        data_dict = map_output(data_dict)
        return return_non_empty(data_dict)
