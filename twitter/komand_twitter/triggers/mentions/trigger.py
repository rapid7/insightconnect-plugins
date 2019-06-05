import komand
import time
from .schema import MentionsInput, MentionsOutput
# Custom imports below
from komand_twitter.util import util


class Mentions(komand.Trigger):

    # Constants
    CACHE_FILE_NAME = "triggers_twitter_mention"
    MAX_MENTION_COUNT = 200  # Max amount supported by Twitter.

    interval = util.Common.SleepDuration.HIGH_ACTIVITY  # Default to high
    pattern = None
    cache_file = None
    cached_id = 0  # The latest ID from the previous fetch.

    def __init__(self):
        super(self.__class__, self).__init__(
            name='mentions',
            description='Monitor for mentions',
            input=MentionsInput(),
            output=MentionsOutput())

    def run(self, params={}):
        if not self.connection.client:
            assert "Run: Twitter API client was None."
            raise Exception("Run: Twitter API client was None.")

        self.pattern = params.get("pattern")

        # Open and auto-close the file to create the cache file on very first start up
        with komand.helper.open_cachefile(self.CACHE_FILE_NAME) as cache_file:
            print("Run: Got or created cache file: {file}".format(file=cache_file))

        # Make doubly sure it defaults to the original value, just in case?
        self.interval = params.get("interval", util.Common.SleepDuration.HIGH_ACTIVITY)

        # Start loop for triggering
        while True:
            self.logger.info("Run: Iterating main loop")

            # Open cache file and read the latest ID from the previous fetch.
            with komand.helper.open_cachefile(self.CACHE_FILE_NAME) as cache_file:
                self.cached_id = cache_file.readline()

            self.logger.info("Run: Cached id is {id}.".format(id=self.cached_id))

            mentions = self.get_mentions()

            if len(mentions) > 0:  # Only trigger if mentions exist.
                self.trigger_on_mentions(mentions=mentions)
                self.logger.info("Run: Trigger done. Sleeping {seconds} seconds.".format(seconds=self.interval))
            else:
                self.logger.info("Run: No new mentions. Sleeping {seconds} seconds.".format(seconds=self.interval))

            time.sleep(self.interval)

    '''Fetches new mentions from Twitter and then sets the sleep time appropriately.'''
    def get_mentions(self):
        mentions = self.connection.client.GetMentions(count=self.MAX_MENTION_COUNT, since_id=self.cached_id)
        mention_count = len(mentions)
        self.logger.info("Get Mentions: Got {count} mentions.".format(count=mention_count))

        if self.pattern:
            mentions = self.filter_mentions(mentions=mentions)

        return mentions

    '''Takes a list of mentions, matches them against the user-supplied pattern, and returns a new list containing
        the filtered mentions'''
    def filter_mentions(self, mentions):
        filtered_mentions = list()

        for mention in mentions:
            if util.Common.matches_pattern(text_to_match=mention.text, pattern=self.pattern):
                filtered_mentions.append(mention)

        return filtered_mentions

    '''Takes a list of mentions and sends triggers for them. Writes the first ID (latest) to cache file.'''
    def trigger_on_mentions(self, mentions):
        for index, mention in enumerate(mentions):
            if index == 0:
                # Write this ID to cache file since it is most up-to-date
                with komand.helper.open_cachefile(self.CACHE_FILE_NAME) as cache_file:
                    cache_file.write(str(mention.id))

            self.logger.info("Trigger On Mentions: Sending trigger for mention {id}.".format(id=mention.id))
            payload = self.create_trigger_payload(mention)
            self.send(payload)

    '''Creates a payload to send from a mention.'''
    def create_trigger_payload(self, mention):
        msg = mention.text.encode('ascii', 'ignore')
        user = mention.user.screen_name.encode('ascii', 'ignore')
        url = "{base_url}/{screen_name}/status/{post_id}".format(base_url=self.connection.TWITTER_URL,
                                                                 screen_name=user,
                                                                 post_id=mention.id)
        payload = {'msg': msg, 'user': user, 'url': url}
        self.logger.info("Create Trigger Payload: Created {payload}".format(payload=payload))
        return payload

    def test(self, params={}):
        """TODO: Test the trigger"""
        return {}
