import re


class Common:

    class SleepDuration:
        LOW_ACTIVITY = 360
        HIGH_ACTIVITY = 60

    '''Takes a string and attempts to match it's text against a user-supplied pattern.'''
    @staticmethod
    def matches_pattern(text_to_match, pattern):
        if not pattern or len(pattern) == 0:  # If pattern is not supplied, then return True
            return True

        if re.match(pattern, text_to_match):  # Pattern was supplied, so try to match
            return True
        else:
            return False

    '''Takes a string and strips out the mention from it by removing the '@' prefixing the username.'''
    @staticmethod
    def strip_mention_out_of_tweet(username, tweet):
        user_mention = "@{username}".format(username=username)

        if user_mention not in tweet:  # If the user (ie. @MyAccount) is not found, return tweet as-is.
            return tweet

        while user_mention in tweet:  # Loop through the tweet until it is totally sanitized
            mention_index = tweet.index(user_mention)
            tweet_chars = list(tweet)
            tweet_chars[mention_index] = ""
            tweet = "".join(tweet_chars)

        return tweet

    '''Determines sleep duration based on a ratio of new mentions to max mention fetch count from the API.'''
    @staticmethod
    def determine_sleep_duration(count, limit):
        percentage_new_mentions = (float(count) / float(limit)) * 100
        if percentage_new_mentions >= 50:  # If count >= 50% limit, return high activity sleep duration.
            return Common.SleepDuration.HIGH_ACTIVITY
        else:
            return Common.SleepDuration.LOW_ACTIVITY