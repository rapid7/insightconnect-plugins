import insightconnect_plugin_runtime
import time
from .schema import MonitorIpsInGreynoiseInput, MonitorIpsInGreynoiseOutput, Input, Output, Component

# Custom imports below

from insightconnect_plugin_runtime.exceptions import PluginException


class MonitorIpsInGreynoise(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_ips_in_greynoise",
            description=Component.DESCRIPTION,
            input=MonitorIpsInGreynoiseInput(),
            output=MonitorIpsInGreynoiseOutput(),
        )

    def _matching_ips(self, query):
        alert_ips = []
        scroll = None
        seen_scrolls = set()
        while True:
            response = self.connection.gn_client.query(query, size=10000, scroll=scroll)
            if not isinstance(response, dict):
                break
            data = response.get("data")
            if isinstance(data, list):
                for item in data:
                    if isinstance(item, dict) and item.get("ip"):
                        alert_ips.append(item["ip"])
            metadata = response.get("request_metadata")
            if not isinstance(metadata, dict) or metadata.get("complete", True):
                break
            scroll = metadata.get("scroll")
            if not scroll or scroll in seen_scrolls:
                break
            seen_scrolls.add(scroll)
        return alert_ips

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        interval = params.get(Input.INTERVAL)
        ip_list = params.get(Input.IP_LIST)
        lookback_days = params.get(Input.LOOKBACK_DAYS)
        # END INPUT BINDING - DO NOT REMOVE

        self.logger.info("Loading GreyNoise Alert Trigger")
        while True:
            try:
                query = f"({' OR '.join(ip_list)}) last_seen:{lookback_days}d"

                self.logger.info("Checking GreyNoise for IP list")
                alert_ip_list = self._matching_ips(query)
                if alert_ip_list:
                    self.logger.info("IPs found in GreyNoise")
                    self.send(
                        {
                            Output.ALERT_IP_LIST: alert_ip_list,
                        }
                    )
            except Exception as error:
                raise PluginException(
                    cause=f"Plugin exception occurred: {error}",
                    assistance="Please check the input and try again.",
                )
            time.sleep(interval)
