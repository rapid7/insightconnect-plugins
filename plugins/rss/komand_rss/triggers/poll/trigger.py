import insightconnect_plugin_runtime
import time
from .schema import PollInput, PollOutput, Input, Output

# Custom imports below
from komand_rss.util.constants import DEFAULT_SLEEPING_TIME, DEFAULT_ENTRY_LIMIT
from typing import List, Dict, Any
import feedparser


class Poll(insightconnect_plugin_runtime.Trigger):
    _CACHE_FILE_NAME = "triggers_rss_poll"

    def __init__(self):
        super(self.__class__, self).__init__(
            name="poll",
            description="Poll feed for latest event",
            input=PollInput(),
            output=PollOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        sleep_duration = params.get(Input.FREQUENCY, DEFAULT_SLEEPING_TIME)
        feed_url = self.connection.feed_url
        # END INPUT BINDING - DO NOT REMOVE

        # Retrieve latest feed published timestamp to begin
        last_entry_timestamp = self.get_latest_entry_timestamp(self.parse_feed(feed_url))

        while True:
            self.logger.info(f"Fetching entries from '{feed_url}'")
            feed = list(
                filter(
                    lambda element: element.get("published_parsed") > last_entry_timestamp, self.parse_feed(feed_url)
                )
            )
            if feed:
                self.logger.info(f"New {len(feed)} entries found. Returning results.")
                for entry in feed:
                    self.send({Output.RESULTS: entry})
                last_entry_timestamp = self.get_latest_entry_timestamp(feed)
            else:
                self.logger.info("No new entries found.")
            self.logger.info(f"Sleeping for {sleep_duration} seconds...")
            time.sleep(sleep_duration)

    @staticmethod
    def parse_feed(feed_url: str) -> List[Dict[str, Any]]:
        """
        Parse the given feed URL and extract a list of objects.

        :param feed_url: The URL of the feed to parse.
        :type: str

        :return: A list of entry objects extracted from the feed.
        :rtype: List[Dict[str, Any]]
        """

        # The [::-1] allows to reverse the returned entries from oldest at [0] index to latest
        # Also, in order to save the memory usage the limitation for the length returned elements was set
        return feedparser.parse(feed_url).get("entries", [])[:DEFAULT_ENTRY_LIMIT][::-1]

    @staticmethod
    def get_latest_entry_timestamp(feed: List[Dict[str, Any]]) -> time.struct_time:
        """
        Get the latest entry timestamp from a feed.

        :param feed: A list of dictionaries representing entries in the feed.
        :type: List[Dict[str, Any]]

        :return: The latest entry timestamp as a struct_time object.
        :rtype: time.struct_time
        """

        return next(reversed(feed), {}).get("published_parsed", time.localtime())
