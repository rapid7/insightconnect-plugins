import insightconnect_plugin_runtime

from .schema import ThreatFeedInput, ThreatFeedOutput, Input, Output, Component

# Custom imports below
from icon_whoisfreaks.util import feed
from icon_whoisfreaks.util.feed_poller import FeedPoller, build_settings, selected_feeds


class ThreatFeed(insightconnect_plugin_runtime.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="threat_feed",
            description=Component.DESCRIPTION,
            input=ThreatFeedInput(),
            output=ThreatFeedOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        batch_size = params.get(Input.BATCH_SIZE)
        catch_up_missed_dates = params.get(Input.CATCH_UP_MISSED_DATES)
        domain_keywords = params.get(Input.DOMAIN_KEYWORDS)
        include_malware = params.get(Input.INCLUDE_MALWARE)
        include_phishing = params.get(Input.INCLUDE_PHISHING)
        include_spam = params.get(Input.INCLUDE_SPAM)
        min_confidence = params.get(Input.MIN_CONFIDENCE)
        poll_interval_minutes = params.get(Input.POLL_INTERVAL_MINUTES)
        start_date = params.get(Input.START_DATE)
        # END INPUT BINDING - DO NOT REMOVE

        feeds = selected_feeds(
            {
                "Include Phishing": (feed.threat_feed("phishing"), include_phishing),
                "Include Malware": (feed.threat_feed("malware"), include_malware),
                "Include Spam": (feed.threat_feed("spam"), include_spam),
            }
        )
        settings = build_settings(
            self.logger,
            feeds,
            batch_size=batch_size,
            poll_interval_minutes=poll_interval_minutes,
            start_date=start_date,
            catch_up=catch_up_missed_dates,
            domain_keywords=domain_keywords,
            min_confidence=min_confidence,
        )
        FeedPoller(self, self.connection.client, feeds, settings).run()
