import insightconnect_plugin_runtime
from .schema import CreateUpdateWatchlistItemsInput, CreateUpdateWatchlistItemsOutput, Input, Output, Component

from icon_azure_sentinel.util.tools import return_non_empty, map_output


class CreateUpdateWatchlistItems(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_update_watchlist_items",
            description=Component.DESCRIPTION,
            input=CreateUpdateWatchlistItemsInput(),
            output=CreateUpdateWatchlistItemsOutput(),
        )

    def run(self, params={}):
        resource_group_name = params.pop(Input.RESOURCEGROUPNAME)
        workspace_name = params.pop(Input.WORKSPACENAME)
        subscription_id = params.pop(Input.SUBSCRIPTIONID)
        watchlist_alias = params.pop(Input.WATCHLISTALIAS)
        watchlist_item_id = params.pop(Input.WATCHLISTITEMID)

        data_dict = self.connection.api_client.create_update_watchlist_items(
            resource_group_name, workspace_name, subscription_id, watchlist_alias, watchlist_item_id, **params
        )
        data_dict = map_output(data_dict)
        return return_non_empty(data_dict)
