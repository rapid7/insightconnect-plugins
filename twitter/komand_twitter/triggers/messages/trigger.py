import komand
import time
from .schema import MessagesInput, MessagesOutput
# Custom imports below
from komand_twitter.util import util


class Messages(komand.Trigger):

    # Constants
    CACHE_FILE_NAME = "triggers_twitter_messages"
    MAX_MENTION_COUNT = 200  # Max amount supported by Twitter.

    interval = util.Common.SleepDuration.HIGH_ACTIVITY  # Default to high
    pattern = None
    cache_file = None
    cached_id = 0  # The latest ID from the previous fetch.

    def __init__(self):
        super(self.__class__, self).__init__(
            name='messages',
            description='Monitor received messages',
            input=MessagesInput(),
            output=MessagesOutput())

    def run(self, params={}):
        if not self.connection.client:
            assert "Run: Twitter API client was None."
            raise Exception("Run: Twitter API client was None.")

        self.pattern = params.get("pattern")

        # Open and auto-close the file to create the cache file on very first start up
        with komand.helper.open_cachefile(self.CACHE_FILE_NAME) as cache_file:
            self.logger.info("Run: Got or created cache file: {file}".format(file=cache_file))

        # Make doubly sure it defaults to the original value, just in case?
        self.interval = params.get("interval", util.Common.SleepDuration.HIGH_ACTIVITY)

        # Start loop for triggering
        while True:
            self.logger.info("Run: Iterating main loop")

            # Open cache file and read the latest ID from the previous fetch.
            with komand.helper.open_cachefile(self.CACHE_FILE_NAME) as cache_file:
                self.cached_id = cache_file.readline()

            self.logger.info("Run: Cached id is {id}.".format(id=self.cached_id))

            messages = self.get_messages()

            if len(messages) > 0:  # Only trigger if messages exist.
                self.trigger_on_messages(messages=messages)
                self.logger.info("Run: Trigger done. Sleeping {seconds} seconds.".format(seconds=self.interval))
            else:
                self.logger.info(
                    "Run: No new messages. Sleeping {seconds} seconds.".format(seconds=self.interval))

            time.sleep(self.interval)

    '''Fetches new messages from Twitter and then sets the sleep time appropriately.'''
    def get_messages(self):
        messages = self.connection.client.GetDirectMessages(count=self.MAX_MENTION_COUNT, since_id=self.cached_id)
        message_count = len(messages)
        self.logger.info("Get Messages: Got {count} messages.".format(count=message_count))

        if self.pattern:
            messages = self.filter_messages(messages=messages)

        return messages

    '''Takes a list of messages, matches them against the user-supplied pattern, and returns a new list containing
        the filtered messages'''
    def filter_messages(self, messages):
        filtered_messages = list()

        for message in messages:
            if util.Common.matches_pattern(text_to_match=message.text, pattern=self.pattern):
                filtered_messages.append(message)

        return filtered_messages

    '''Takes a list of messages and sends triggers for them. Writes the first ID (latest) to cache file.'''
    def trigger_on_messages(self, messages):
        for index, message in enumerate(messages):
            if index == 0:
                # Write this ID to cache file since it is most up-to-date
                with komand.helper.open_cachefile(self.CACHE_FILE_NAME) as cache_file:
                    cache_file.write(str(message.id))

            self.logger.info("Trigger On Messages: Sending trigger for message {id}.".format(id=message.id))
            payload = self.create_trigger_payload(message)
            self.send(payload)

    '''Creates a a payload to send from a message.'''
    def create_trigger_payload(self, message):
        payload = {
            'msg': message.text.encode('ascii', 'ignore'),
            'user': message.sender_screen_name.encode('ascii', 'ignore'),
            # Cast to string to mitigate long integer bug in product
            'id': str(message.id),
            'created_at': message.created_at.encode('ascii', 'ignore'),
            'sender_id': message.sender_id,
            'sender_created_at': message.sender.created_at.encode('ascii', 'ignore'),
            'sender_default_profile': message.sender.default_profile,
            'sender_default_profile_image': message.sender.default_profile_image,
            'sender_description': message.sender.description.encode('ascii', 'ignore'),
            'sender_followers_count': message.sender.followers_count,
            'sender_friends_count': message.sender.friends_count,
            'sender_lang': message.sender.lang.encode('ascii', 'ignore'),
            'sender_location': message.sender.location.encode('ascii', 'ignore'),
            'sender_name': message.sender.name.encode('ascii', 'ignore'),
            'recipient_id': message.recipient_id
        }
        self.logger.info("Create Trigger Payload: Created {payload}".format(payload=payload))
        return payload

    def test(self, params={}):
        """TODO: Test the trigger"""
        return {}
