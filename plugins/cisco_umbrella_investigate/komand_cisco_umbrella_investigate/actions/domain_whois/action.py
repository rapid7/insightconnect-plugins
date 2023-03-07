import insightconnect_plugin_runtime
from .schema import DomainWhoisInput, DomainWhoisOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class DomainWhois(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="domain_whois",
            description="A standard WHOIS response record for a single domain with all available WHOIS data returned in an array",
            input=DomainWhoisInput(),
            output=DomainWhoisOutput(),
        )

    def run(self, params={}):
        domain = params.get(Input.DOMAIN)
        try:
            domain_whois = self.connection.investigate.domain_whois(domain)
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        return {Output.WHOIS: [domain_whois]}
