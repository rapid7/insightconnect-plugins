import insightconnect_plugin_runtime

from .schema import NewlyRegisteredDomainsInput, NewlyRegisteredDomainsOutput, Input, Output, Component

# Custom imports below
from icon_whoisfreaks.util import feed
from icon_whoisfreaks.util.feed_poller import FeedPoller, build_settings, selected_feeds


class NewlyRegisteredDomains(insightconnect_plugin_runtime.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="newly_registered_domains",
            description=Component.DESCRIPTION,
            input=NewlyRegisteredDomainsInput(),
            output=NewlyRegisteredDomainsOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        batch_size = params.get(Input.BATCH_SIZE)
        catch_up_missed_dates = params.get(Input.CATCH_UP_MISSED_DATES)
        domain_keywords = params.get(Input.DOMAIN_KEYWORDS)
        include_country_code_tlds = params.get(Input.INCLUDE_COUNTRY_CODE_TLDS)
        include_generic_tlds = params.get(Input.INCLUDE_GENERIC_TLDS)
        include_whois = params.get(Input.INCLUDE_WHOIS)
        poll_interval_minutes = params.get(Input.POLL_INTERVAL_MINUTES)
        start_date = params.get(Input.START_DATE)
        tld_filter = params.get(Input.TLD_FILTER)
        # END INPUT BINDING - DO NOT REMOVE

        feeds = selected_feeds(
            {
                "Include Generic TLDs": (feed.nrd_feed("gtld", bool(include_whois)), include_generic_tlds),
                "Include Country-Code TLDs": (feed.nrd_feed("cctld", bool(include_whois)), include_country_code_tlds),
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
            tld_filter=tld_filter,
        )
        FeedPoller(self, self.connection.client, feeds, settings).run()
