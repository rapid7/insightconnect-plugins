import insightconnect_plugin_runtime
from .schema import LatestDomainsInput, LatestDomainsOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from IPy import IP as IP_Validate


class LatestDomains(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="latest_domains",
            description="Return associated malicious domains for an IP address",
            input=LatestDomainsInput(),
            output=LatestDomainsOutput(),
        )

    def run(self, params={}):
        ip_address = params.get(Input.IP)
        try:
            IP_Validate(ip_address)
        except Exception as error:
            raise PluginException(
                cause="Invalid IP provided by user.",
                assistance="Please try again by submitting a valid IP address.",
                data=error,
            )

        try:
            latest_domains = self.connection.investigate.latest_domains(ip_address)
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
        return {Output.DOMAINS: latest_domains}
