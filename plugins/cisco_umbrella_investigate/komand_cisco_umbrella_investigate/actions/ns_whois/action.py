import insightconnect_plugin_runtime
from .schema import NsWhoisInput, NsWhoisOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class NsWhois(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="ns_whois",
            description="Allows you to search a nameserver to find all domains registered by that nameserver",
            input=NsWhoisInput(),
            output=NsWhoisOutput(),
        )

    def run(self, params={}):
        nameserver = params.get(Input.NAMESERVER)
        try:
            ns_whois = self.connection.investigate.ns_whois([nameserver], limit=1000)
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
        one_ns_whois = ns_whois.get(nameserver)
        if not one_ns_whois:
            raise PluginException(cause="Invalid nameserver.", assistance="Unable to to retrieve domains.")
        return {
            Output.DOMAIN: [
                {
                    "more_data_available": one_ns_whois.get("moreDataAvailable"),
                    "limit": one_ns_whois.get("limit"),
                    "domains": one_ns_whois.get("domains"),
                    "total_results": one_ns_whois.get("totalResults"),
                }
            ]
        }
