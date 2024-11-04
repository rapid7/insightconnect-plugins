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

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        interval = params.get(Input.INTERVAL)
        ip_list = params.get(Input.IP_LIST)
        lookback_days = params.get(Input.LOOKBACK_DAYS)
        # END INPUT BINDING - DO NOT REMOVE

        self.logger.info("Loading GreyNoise Alert Trigger")
        while True:
            try:
                query_ips = ""
                counter = 0
                for ip in ip_list:
                    if counter == 0:
                        query_ips = "(" + str(ip)
                        counter = counter + 1
                    else:
                        query_ips = query_ips + " OR " + str(ip)
                        counter = counter + 1
                query_ips = query_ips + ")"

                self.logger.info("Checking GreyNoise for IP list")
                query = query_ips + " last_seen:" + str(lookback_days) + "d"
                response = self.connection.gn_client.query(query)

                if response.get("count") != 0:
                    self.logger.info("IPs found in GreyNoise")
                    alert_ip_list = []
                    for item in response["data"]:
                        alert_ip_list.append(item["ip"])
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
