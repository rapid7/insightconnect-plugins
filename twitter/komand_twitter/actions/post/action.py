import komand
from .schema import PostInput, PostOutput
from komand.exceptions import PluginException
# Custom imports below
from komand_twitter.util import util


class Post(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='post',
                description='Tweet',
                input=PostInput(),
                output=PostOutput())

    def run(self, params={}):
        tweet = params.get("msg")

        self.logger.info("Run: Tweet is: " + tweet)

        tweet_length = len(tweet)
        self.logger.info("Run: Tweet length is {tweet_length}".format(tweet_length=tweet_length))

        if tweet_length == 0:
            assert "Run: Tweet length was 0. Make sure property 'msg' is marked required."
            raise PluginException(cause='Twitter: Tweet length was 0. Make sure property \'msg\' is marked required.')

        if tweet_length > self.connection.TWEET_MAX_LENGTH:  # Requirement: Truncate tweet is greater than max length
            self.logger.info("Run: Tweet was greater than maximum allowed length by Twitter ({length}/{max_length}). "
                         "Tweet will be truncated")\
                .format(length=tweet_length, max_length=self.connection.TWEET_MAX_LENGTH)
            tweet = tweet[:self.connection.TWEET_MAX_LENGTH]

        tweet = util.Common.strip_mention_out_of_tweet(username=self.connection.screen_name, tweet=tweet)
        post = self.connection.client.PostUpdate(tweet).AsDict()

        if not post:
            assert "Run: No payload received."
            raise PluginException(cause='Twitter: No response received from API request.')

        post_id = post.get("id")

        post_url = "{base_url}/{screen_name}/status/{post_id}".format(base_url=self.connection.TWITTER_URL,
                                                                      screen_name=self.connection.screen_name,
                                                                      post_id=post_id)
        self.logger.info("Run: Post successful!")
        return {'url': post_url}

    def test(self, params={}):
        """TODO: Test action"""
        #
        return {} 
