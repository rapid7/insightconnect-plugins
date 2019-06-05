import komand
import time
from .schema import PollInput, PollOutput
# Custom imports below
import feedparser


class Poll(komand.Trigger):
    
    _CACHE_FILE_NAME = "triggers_rss_poll"

    def __init__(self):
        super(self.__class__, self).__init__(
                name='poll',
                description='Poll feed for latest event',
                input=PollInput(),
                output=PollOutput())

    def run(self, params={}):
        sleep_duration = params.get("frequency")

        # Open and auto-close the file to create the cache file on very first start up
        with komand.helper.open_cachefile(self._CACHE_FILE_NAME):
            self.logger.info("Run: Got or created cache file")

        while True:
            self.logger.info("Run: Fetching entries from {feed_url}".format(feed_url=self.connection.FEED_URL))
            feed = feedparser.parse(self.connection.FEED_URL)
            new_count = 0  # Keep track of number of new entries

            with komand.helper.open_cachefile(self._CACHE_FILE_NAME) as cache_file:
                for entry in feed.entries:
                    cache_file.seek(0)  # Ensure pointer is back at start
                    link = entry["link"]  # Use link as an identifier since it is guaranteed according to W3 RSS spec

                    if link in cache_file.read().splitlines():  # If entry previously parsed, skip to next
                        self.logger.info("Run: Skipping previously parsed entry")
                        continue

                    self.logger.info("Run: New entry found, parsing")
                    payload = self.create_payload_from_entry(entry)

                    new_count += 1
                    cache_file.write("{link}\n".format(link=link))
                    self.send(payload)

            self.logger.info("Run: Parsed {new} new entries. Sleeping for {sleep} seconds.".format(new=new_count,
                                                                                                   sleep=sleep_duration))
            time.sleep(sleep_duration)

    @staticmethod
    def create_payload_from_entry(entry):
        # This method can be improved using priority/fallback properties on an RSS entry.
        # See https://cyber.harvard.edu/rss/rss.html#requiredChannelElements for info on required/optional elements.

        return {'results': entry}

    def test(self):
        feed = feedparser.parse(self.connection.FEED_URL)

        for entry in feed.entries:
            link = entry["link"]  # Use link as an identifier since it is guaranteed according to W3 RSS spec
            return self.create_payload_from_entry(entry)

        return {"contents": "http://example.com", "description": "Hello, world", 'title': "Example entry"}
