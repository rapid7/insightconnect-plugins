import insightconnect_plugin_runtime
from .schema import CreateUpdateWatchlistInput, CreateUpdateWatchlistOutput, Input, Output, Component


class CreateUpdateWatchlist(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_update_watchlist",
            description=Component.DESCRIPTION,
            input=CreateUpdateWatchlistInput(),
            output=CreateUpdateWatchlistOutput(),
        )

    def run(self, params={}):
        subscription_id = params.pop(Input.SUBSCRIPTIONID)
        resource_group_name = params.pop(Input.RESOURCEGROUPNAME)
        workspace_name = params.pop(Input.WORKSPACENAME)
        watchlist_alias = params.pop(Input.WATCHLISTALIAS)
        data_dict = self.connection.api_client.create_update_watchlist(
            resource_group_name, workspace_name, watchlist_alias, subscription_id, **params
        )
        return {Output.WATCHLIST: data_dict}
