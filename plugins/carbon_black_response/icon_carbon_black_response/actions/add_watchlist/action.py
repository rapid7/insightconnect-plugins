import insightconnect_plugin_runtime
from .schema import AddWatchlistInput, AddWatchlistOutput

# Custom imports below
from cbapi.errors import ServerError
from cbapi.response.models import Watchlist


class AddWatchlist(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_watchlist",
            description="Adds a watchlist",
            input=AddWatchlistInput(),
            output=AddWatchlistOutput(),
        )

    def run(self, params={}):
        watchlist = self.connection.carbon_black.create(
            Watchlist, data={"name": params["name"], "index_type": params["index_type"]}
        )
        watchlist.query = params["query"]

        self.logger.debug("Adding watchlist: {0:s}".format(str(watchlist)))

        try:
            watchlist.save()
        except ServerError as se:
            self.logger.error("Could not add watchlist: {0:s}".format(str(se)))
            raise se
        except Exception as ex:
            self.logger.error("Could not add watchlist: {0:s}".format(str(ex)))
            raise ex
        else:
            self.logger.debug("Watchlist data: {0:s}".format(str(watchlist)))
            self.logger.info("Added watchlist. New watchlist ID is {0:s}".format(str(watchlist.id)))
        return {"id": str(watchlist.id)}

    def test(self):
        if self.connection.test():
            return {}
