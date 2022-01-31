import insightconnect_plugin_runtime
from .schema import DeleteFeedInput, DeleteFeedOutput

# Custom imports below
from cbapi.response.models import Feed


class DeleteFeed(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_feed", description="", input=DeleteFeedInput(), output=DeleteFeedOutput()
        )

    def run(self, params={}):
        feed_id = params["id"]
        force_deletion = params["force"]
        attempted_to_find = "ID of {0:s}".format(feed_id)

        try:
            feeds = [self.connection.carbon_black.select(Feed, feed_id, force_init=True)]
            if not feeds:
                self.logger.info("No feeds were found that match the specified feed ID!")
                return {"success": False}
        except Exception as e:
            raise Exception("Error: {error}\n Please contact support for assistance.".format(error=e))

        if len(feeds) > 1 and not force_deletion:
            self.logger.error(
                "Warning: Multiple feeds with ID {id} found. Stopping. Please enable force deletion "
                "if you would like to continue."
            )
            return {"success": False}

        for feed in feeds:
            try:
                feed.delete()
            except Exception:
                self.logger.error("Error: Unable to delete feed ID {id}".format(id=attempted_to_find))
                return {"success": False}

            self.logger.info("Success: Deleted feed {name} with ID {id}".format(name=feed.name, id=feed.id))
            return {"success": True}

    def test(self):
        if self.connection.test():
            return {"success": True}
