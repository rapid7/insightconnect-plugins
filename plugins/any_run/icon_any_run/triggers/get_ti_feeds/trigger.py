import insightconnect_plugin_runtime
import time
from .schema import GetTiFeedsInput, GetTiFeedsOutput, Input, Output, Component

# Custom imports below
from anyrun.connectors import FeedsConnector
from anyrun import RunTimeException
from datetime import datetime, timedelta
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_any_run.util.config import Config
from icon_any_run.util.tools import get_indicators


class GetTiFeeds(insightconnect_plugin_runtime.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_ti_feeds", description=Component.DESCRIPTION, input=GetTiFeedsInput(), output=GetTiFeedsOutput()
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        feed_fetch_depth = params.get(Input.FEED_FETCH_DEPTH, 120)
        feed_fetch_interval = params.get(Input.FEED_FETCH_INTERVAL, 90)
        threat_feed_access_key = params.get(Input.THREAT_FEED_ACCESS_KEY, "")
        # END INPUT BINDING - DO NOT REMOVE

        while True:
            self.logger.info("[ANY.RUN] Initialized TI Feeds enrichment.")
            try:
                with FeedsConnector(self.connection.feeds_api_key, integration=Config.VERSION) as connector:
                    self.logger.info("[ANY.RUN] Authentication is passed.")

                    domains = get_indicators(connector, "domain", feed_fetch_depth)
                    ips = get_indicators(connector, "ip", feed_fetch_depth)
                    urls = get_indicators(connector, "url", feed_fetch_depth)

                    self.logger.info(
                        f"[ANY.RUN] TI Feeds are fetched.\nReceived:"
                        f" {len(domains)} domains,"
                        f" {len(ips)} ips,"
                        f" {len(urls)} urls."
                    )

                if domains or ips or urls:
                    self.send(
                        {
                            Output.ANYRUN_FEED_DOMAINS: domains,
                            Output.ANYRUN_FEED_IPS: ips,
                            Output.ANYRUN_FEED_URLS: urls,
                            Output.THREAT_FEED_ACCESS_KEY: threat_feed_access_key,
                        }
                    )

                self.logger.info(
                    f"[ANY.RUN] Trigger executed successfully. "
                    f"Next run at: {datetime.now() + timedelta(seconds=feed_fetch_interval * 60)}."
                )

                time.sleep(feed_fetch_interval * 60)

            except RunTimeException as error:
                raise PluginException(
                    cause="Failed to start analysis.",
                    assistance=error.description,
                    data=error.json,
                )
