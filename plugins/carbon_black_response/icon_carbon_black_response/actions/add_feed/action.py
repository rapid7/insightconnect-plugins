import insightconnect_plugin_runtime
from .schema import AddFeedInput, AddFeedOutput

# Custom imports below
from cbapi.errors import ServerError
from cbapi.response.models import Feed


class AddFeed(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_feed", description="Adds a feed", input=AddFeedInput(), output=AddFeedOutput()
        )

    def run(self, params={}):
        feed_url = params["feed_url"]
        configured_feeds = [f for f in self.connection.carbon_black.select(Feed) if f.feed_url == feed_url]
        if configured_feeds:
            self.logger.info("Warning: Feeds already configured for this url: {0:s}:".format(feed_url))
            for feed in configured_feeds:
                self.logger.info(feed)
            if not params["force"]:
                return

        feed = self.connection.carbon_black.create(Feed)
        feed.feed_url = feed_url
        if params["enabled"] is not None:
            feed.enabled = params["enabled"]

        if len(params["username"]) > 0:
            feed.username = params["username"]
        if len(params["password"]) > 0:
            feed.password = params["password"]

        if len(params["cert"]) > 0:
            feed.ssl_client_crt = params["cert"]["content"]
        if len(params["key"]) > 0:
            feed.ssl_client_key = params["key"]["content"]

        if params["use_proxy"] is not None:
            feed.use_proxy = params["use_proxy"]

        if params["validate_server_cert"] is not None:
            feed.validate_server_cert = params["validate_server_cert"]

        self.logger.debug("Adding feed: {0:s}".format(str(feed)))

        try:
            feed.save()
        except ServerError as se:
            if se.error_code == 500:
                self.logger.error("Could not add feed:")
                self.logger.error(
                    " Received error code 500 from server. This is usually because the server cannot retrieve the feed."
                )
                self.logger.error(
                    " Check to ensure the Cb server has network connectivity and the credentials are correct."
                )
            else:
                self.logger.error("Could not add feed: {0:s}".format(str(se)))
            raise se
        except Exception as ex:
            self.logger.error("Could not add feed: {0:s}".format(str(ex)))
            raise ex
        else:
            self.logger.debug("Feed data: {0:s}".format(str(feed)))
            self.logger.info("Added feed. New feed ID is {0:d}".format(feed.id))
            return {"id": feed.id}

    def test(self):
        if self.connection.test():
            return {}
