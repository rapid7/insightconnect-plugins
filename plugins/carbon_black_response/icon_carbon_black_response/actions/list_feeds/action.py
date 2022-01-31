import insightconnect_plugin_runtime
from .schema import ListFeedsInput, ListFeedsOutput

# Custom imports below


class ListFeeds(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_feeds",
            description="List all feeds",
            input=ListFeedsInput(),
            output=ListFeedsOutput(),
        )

    def run(self, params={}):
        try:
            results = self.connection.carbon_black.get_object("/api/v1/feed")
        except Exception as ex:
            self.logger.error("Failed to get alerts: %s", ex)
            raise ex

        results = insightconnect_plugin_runtime.helper.clean(results)
        return {"feeds": results}

    def test(self):
        if self.connection.test():
            return {}
