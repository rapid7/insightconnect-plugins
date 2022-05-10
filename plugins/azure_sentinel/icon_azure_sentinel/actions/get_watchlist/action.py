import insightconnect_plugin_runtime
from .schema import GetWatchlistInput, GetWatchlistOutput, Input, Output, Component

# Custom imports below


class GetWatchlist(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_watchlist",
            description=Component.DESCRIPTION,
            input=GetWatchlistInput(),
            output=GetWatchlistOutput(),
        )

    def run(self, params={}):
        subscription_id = params.pop(Input.SUBSCRIPTIONID)
        resource_group_name = params.pop(Input.RESOURCEGROUPNAME)
        workspace_name = params.pop(Input.WORKSPACENAME)
        watchlist_alias = params.pop(Input.WATCHLISTALIAS)
        data_dict = self.connection.api_client.get_watchlist(
            resource_group_name, workspace_name, watchlist_alias, subscription_id
        )
        return {Output.WATCHLIST: data_dict}
