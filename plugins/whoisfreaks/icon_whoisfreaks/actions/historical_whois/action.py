import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import HistoricalWhoisInput, HistoricalWhoisOutput, Input, Output, Component

# Custom imports below
from icon_whoisfreaks.util import constants, outputs, validators


class HistoricalWhois(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="historical_whois",
            description=Component.DESCRIPTION,
            input=HistoricalWhoisInput(),
            output=HistoricalWhoisOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        domain = params.get(Input.DOMAIN)
        # END INPUT BINDING - DO NOT REMOVE

        result = self.connection.client.lookup(
            "Historical WHOIS", "GET", constants.PATH_HISTORICAL_WHOIS, {"domainName": validators.domain(domain)}
        )
        return outputs.paged(result, "whois_domains_historical", ("total_records",), (), ())
