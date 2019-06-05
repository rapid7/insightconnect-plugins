import komand
from .schema import ConnectionSchema
# Custom imports below
import twitter


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.TWITTER_URL = 'https://twitter.com'
        self.TWEET_MAX_LENGTH = 140
        self.screen_name = None
        self.client = None

    def connect(self, params={}):
        self.logger.info("Connect: Creating Twitter client.")

        access_token = params['access_token_credentials']['username']
        access_token_secret = params['access_token_credentials']['password']
        consumer_key = params['consumer_credentials']['username']
        consumer_secret = params['consumer_credentials']['password']

        assert access_token is not None or len(access_token) == 0, \
            "Connect: Property 'access_token' was None or 0 length. Make sure it is marked required."
        assert access_token_secret is not None or len(access_token_secret) == 0, \
            "Connect: Property 'access_token_secret' was None or 0 length. Make sure it is marked required."
        assert consumer_key is not None or len(consumer_key) == 0, \
            "Connect: Property 'consumer_key' was None or 0 length. Make sure it is marked required."
        assert consumer_secret is not None or len(consumer_secret) == 0, \
            "Connect: Property 'consumer_secret' was None or 0 length. Make sure it is marked required."

        self.logger.info("Right about to create API client")

        client = twitter.Api(consumer_key=consumer_key,
                             consumer_secret=consumer_secret,
                             access_token_key=access_token,
                             access_token_secret=access_token_secret,
                             sleep_on_rate_limit=True)

        self.logger.info("API Client created")

        self.client = client
        assert client is not None, "Connect: Twitter API client was None."

        # TODO: Verify connection was successful
        verification_info = client.VerifyCredentials().AsDict()

        username = verification_info.get("name")
        user_id = verification_info.get("id")
        self.screen_name = verification_info.get("screen_name")

        assert username is not None and user_id is not None and self.screen_name is not None, \
            "Connect: One or more necessary properties not found. Unsure of success."

        self.logger.info("Connect: Connected! ID: {id}, "
                     "Username: {username}, "
                     "ScreenName: {screen_name}".format(id=user_id,
                                                        username=username,
                                                        screen_name=self.screen_name))
