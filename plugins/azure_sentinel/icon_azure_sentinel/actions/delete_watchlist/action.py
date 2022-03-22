import insightconnect_plugin_runtime
from .schema import DeleteWatchlistInput, DeleteWatchlistOutput, Input, Output, Component

# Custom imports below


class DeleteWatchlist(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_watchlist",
            description=Component.DESCRIPTION,
            input=DeleteWatchlistInput(),
            output=DeleteWatchlistOutput(),
        )

    def run(self, params={}):
        subscription_id = params.pop(Input.SUBSCRIPTIONID)
        resource_group_name = params.pop(Input.RESOURCEGROUPNAME)
        workspace_name = params.pop(Input.WORKSPACENAME)
        watchlist_alias = params.pop(Input.WATCHLISTALIAS)
        status_code = self.connection.api_client.delete_watchlist(
            resource_group_name, workspace_name, watchlist_alias, subscription_id
        )
        return {Output.STATUS: status_code}
