import insightconnect_plugin_runtime
import time
from .schema import GreynoiseAlertInput, GreynoiseAlertOutput, Input, Output, Component
# Custom imports below

from insightconnect_plugin_runtime.exceptions import PluginException


class GreynoiseAlert(insightconnect_plugin_runtime.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="greynoise_alert",
                description=Component.DESCRIPTION,
                input=GreynoiseAlertInput(),
                output=GreynoiseAlertOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        interval = params.get(Input.INTERVAL, 3600)
        ip_list = params.get(Input.IP_LIST)
        lookback_days = params.get(Input.LOOKBACK_DAYS)
        # END INPUT BINDING - DO NOT REMOVE

        while True:
            query_ips = ""
            counter = 0
            for ip in ip_list:
                if counter == 0:
                    query_ips = str(ip)
                    counter = counter + 1
                else:
                    query_ips = query_ips + " OR " + str(ip)
                    counter = counter + 1
            try:
                int(lookback_days)
            except Exception:
                raise PluginException(
                    cause=f"Lookback Days value is not a valid integer.",
                    assistance="Please check the input and try again.",
                )

            query = query_ips + "last_seen:" + str(lookback_days) + "d"
            response = self.connection.gn_client.query(query)

            if response.get(count) != "0":
                alert_ip_list = []
                for item in response["data"]:
                    alert_ip_list.append(item["ip"])
                self.send({
                    Output.IP_LIST: alert_ip_list,
                })
            time.sleep(interval)
