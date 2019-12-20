import komand
import time
from .schema import TweetsInput, TweetsOutput
# Custom imports below
from komand_twitter.util import util


class Tweets(komand.Trigger):

    # Constants
    CACHE_FILE_NAME = "triggers_twitter_tweets"
    MAX_TWEET_COUNT = 100  # Max amount supported by Twitter.

    interval = util.Common.SleepDuration.HIGH_ACTIVITY  # Default to high
    cache_file = None
    cached_id = 0  # The latest ID from the previous fetch.

    pattern = None  # The required pattern from the user to search with

    def __init__(self):
        super(self.__class__, self).__init__(
            name='tweets',
            description='Monitor for tweets of interest',
            input=TweetsInput(),
            output=TweetsOutput())

    def run(self, params={}):
        if not self.connection.client:
            assert "Run: Twitter API client was None."
            raise Exception("Run: Twitter API client was None.")

        self.pattern = params.get("pattern")
        if not self.pattern:
            assert "Run: Pattern parameter was empty. Make sure input is marked required."
            raise Exception("Run: Pattern parameter was empty. Make sure input is marked required.")

        # Make doubly sure it defaults to the original value, just in case?
        self.interval = params.get("interval", util.Common.SleepDuration.HIGH_ACTIVITY)

        # Open and auto-close the file to create the cache file on very first start up
        with komand.helper.open_cachefile(self.CACHE_FILE_NAME) as cache_file:
            self.logger("Run: Got or created cache file: {file}".format(file=cache_file))

        while True:
            self.logger.info("Run: Iterating main loop")

            # Open cache file and read the latest ID from the previous fetch.
            with komand.helper.open_cachefile(self.CACHE_FILE_NAME) as cache_file:
                self.cached_id = cache_file.readline()

            self.logger.info("Run: Cached id is {id}.".format(id=self.cached_id))

            tweets = self.get_tweets()

            if len(tweets) > 0:  # Only trigger if tweets exist.
                self.trigger_on_tweets(tweets=tweets)
                self.logger.info("Run: Trigger done. Sleeping {seconds} seconds.".format(seconds=self.interval))
            else:
                self.logger.info("Run: No new tweets. Sleeping {seconds} seconds.".format(seconds=self.interval))

            time.sleep(self.interval)

    '''Fetches new tweets from Twitter based on the pattern supplied and then sets the sleep time appropriately.'''
    def get_tweets(self):
        tweets = self.connection.client.GetSearch(term=self.pattern,
                                                  since_id=self.cached_id,
                                                  count=self.MAX_TWEET_COUNT)
        tweet_count = len(tweets)
        self.logger.info("Get Tweets: Got {count} tweets.".format(count=tweet_count))

        return tweets

    '''Takes a list of tweets and sends triggers for them. Writes the first ID (latest) to cache file.'''
    def trigger_on_tweets(self, tweets):
        for index, tweet in enumerate(tweets):
            if index == 0:
                # Write this ID to cache file since it is most up-to-date
                with komand.helper.open_cachefile(self.CACHE_FILE_NAME) as cache_file:
                    cache_file.write(str(tweet.id))

            self.logger.info("Trigger On Tweets: Sending trigger for tweet {id}.".format(id=tweet.id))
            payload = self.create_trigger_payload(tweet)
            self.send(payload)

    '''Creates a a payload to send from a tweet.'''
    def create_trigger_payload(self, tweet):
        msg = tweet.text.encode('ascii', 'ignore')
        user = tweet.user.screen_name.encode('ascii', 'ignore')
        url = "{base_url}/{screen_name}/status/{post_id}".format(base_url=self.connection.TWITTER_URL,
                                                                 screen_name=user,
                                                                 post_id=tweet.id)
        payload = {'msg': msg, 'url': url, 'user': user}
        self.logger.info("Create Trigger Payload: Created {payload}".format(payload=payload))
        return payload

    def test(self, params={}):
        """TODO: Test the trigger"""
        return {}
