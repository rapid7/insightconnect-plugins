import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import BulkWhoisInput, BulkWhoisOutput, Input, Output, Component

# Custom imports below
from icon_whoisfreaks.util import constants, outputs, validators


class BulkWhois(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="bulk_whois",
            description=Component.DESCRIPTION,
            input=BulkWhoisInput(),
            output=BulkWhoisOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        domains = params.get(Input.DOMAINS)
        # END INPUT BINDING - DO NOT REMOVE

        valid, skipped = validators.bulk(domains, validators.try_domain, "Domains")
        if not valid:
            return outputs.bulk(None, None, skipped)
        result = self.connection.client.lookup(
            "Bulk WHOIS", "POST", constants.PATH_BULK_WHOIS, body={"domainNames": valid}
        )
        return outputs.bulk(result, "bulk_whois_response", skipped)
