import insightconnect_plugin_runtime
from .schema import DeleteWatchlistInput, DeleteWatchlistOutput

# Custom imports below
from cbapi.response.models import Watchlist


class DeleteWatchlist(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_watchlist",
            description="",
            input=DeleteWatchlistInput(),
            output=DeleteWatchlistOutput(),
        )

    def run(self, params={}):
        watchlist_id = params["id"]
        force_deletion = params["force"]

        try:
            watchlists = [self.connection.carbon_black.select(Watchlist, watchlist_id, force_init=True)]
            if not watchlists:
                self.logger.info("No watchlists were found that match the specified watchlist ID!")
                return {"success": False}
        except Exception as e:
            raise Exception(f"Error: {e}\n Please contact support for assistance.")

        if len(watchlists) > 1 and not force_deletion:
            self.logger.error(
                "Warning: Multiple watchlists with ID {id} found. Stopping. Please enable force deletion "
                "if you would like to continue."
            )
            return {"success": False}

        for watchlist in watchlists:
            try:
                watchlist.delete()
            except Exception:
                self.logger.error(f"Error: Unable to delete watchlist ID {watchlist.name}")
                return {"success": False}

            self.logger.info(f"Success: Deleted watchlist {watchlist.name} with ID {watchlist.id}")
            return {"success": True}

    def test(self):
        if self.connection.test():
            return {"success": True}
