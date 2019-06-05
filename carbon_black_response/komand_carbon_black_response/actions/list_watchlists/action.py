import komand
from .schema import ListWatchlistsInput, ListWatchlistsOutput
# Custom imports below


class ListWatchlists(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_watchlists',
                description='List all watchlists',
                input=ListWatchlistsInput(),
                output=ListWatchlistsOutput())

    def run(self, params={}):
        try:
            results = self.connection.carbon_black.get_object("/api/v1/watchlist")
        except Exception as ex:
            self.logger.error('Failed to get alerts: %s', ex)
            raise ex

        results = komand.helper.clean(results)

        return {'watchlists': results}

    def test(self):
        if self.connection.test():
            return {}
