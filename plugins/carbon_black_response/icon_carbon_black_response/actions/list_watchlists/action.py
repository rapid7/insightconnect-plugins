import insightconnect_plugin_runtime
from .schema import ListWatchlistsInput, ListWatchlistsOutput

# Custom imports below


class ListWatchlists(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_watchlists",
            description="List all watchlists",
            input=ListWatchlistsInput(),
            output=ListWatchlistsOutput(),
        )

    def run(self):
        try:
            results = self.connection.carbon_black.get_object("/api/v1/watchlist")
        except Exception as ex:
            self.logger.error(f"Failed to get alerts: {ex}")
            raise ex

        results = insightconnect_plugin_runtime.helper.clean(results)

        return {"watchlists": results}

    def test(self):
        if self.connection.test():
            return {}
