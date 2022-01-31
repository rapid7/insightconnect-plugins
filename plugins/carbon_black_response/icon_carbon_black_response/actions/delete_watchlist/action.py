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
            raise Exception("Error: {error}\n Please contact support for assistance.".format(error=e))

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
                self.logger.error("Error: Unable to delete watchlist ID {id}".format(id=watchlist.name))
                return {"success": False}

            self.logger.info(
                "Success: Deleted watchlist {name} with ID {id}".format(name=watchlist.name, id=watchlist.id)
            )
            return {"success": True}

    def test(self):
        if self.connection.test():
            return {"success": True}
