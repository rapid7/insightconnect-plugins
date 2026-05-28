import insightconnect_plugin_runtime
import time
from .schema import AnyrunTiFeedsEnrichmentInput, AnyrunTiFeedsEnrichmentOutput, Input, Output, Component

# Custom imports below
from anyrun.connectors import FeedsConnector

from icon_any_run.util.config import Config
from icon_any_run.util.tools import get_indicators


class AnyrunTiFeedsEnrichment(insightconnect_plugin_runtime.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="anyrun_ti_feeds_enrichment",
            description=Component.DESCRIPTION,
            input=AnyrunTiFeedsEnrichmentInput(),
            output=AnyrunTiFeedsEnrichmentOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        feed_fetch_depth = params.get(Input.FEED_FETCH_DEPTH)
        feed_fetch_interval = params.get(Input.FEED_FETCH_INTERVAL)
        threat_feed_access_key = params.get(Input.THREAT_FEED_ACCESS_KEY)
        # END INPUT BINDING - DO NOT REMOVE

        while True:
            with FeedsConnector(self.connection.feeds_api_key, integration=Config.VERSION) as connector:
                domains = get_indicators(connector, "domain", feed_fetch_depth)
                ips = get_indicators(connector, "ip", feed_fetch_depth)
                urls = get_indicators(connector, "url", feed_fetch_depth)

            self.send(
                {
                    Output.ANYRUN_FEED_DOMAINS: domains,
                    Output.ANYRUN_FEED_IPS: ips,
                    Output.ANYRUN_FEED_URLS: urls,
                    Output.THREAT_FEED_ACCESS_KEY: threat_feed_access_key,
                }
            )

            time.sleep(feed_fetch_interval * 60)
