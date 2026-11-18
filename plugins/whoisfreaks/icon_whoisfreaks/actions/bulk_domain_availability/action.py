import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import BulkDomainAvailabilityInput, BulkDomainAvailabilityOutput, Input, Output, Component

# Custom imports below
from icon_whoisfreaks.util import constants, outputs, validators


class BulkDomainAvailability(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="bulk_domain_availability",
            description=Component.DESCRIPTION,
            input=BulkDomainAvailabilityInput(),
            output=BulkDomainAvailabilityOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        domain = params.get(Input.DOMAIN)
        domains = params.get(Input.DOMAINS)
        tlds = params.get(Input.TLDS)
        # END INPUT BINDING - DO NOT REMOVE

        base_domain = validators.optional_text(domain)
        if domains and (base_domain or tlds):
            raise validators.input_error(
                "Bulk Domain Availability received both Domains and Domain with TLDs",
                "Use either Domains, or Domain together with TLDs",
            )
        if domains:
            valid, skipped = validators.bulk(domains, validators.try_domain, "Domains")
            params, body = None, {"domainNames": valid}
        elif base_domain and tlds:
            valid, skipped = validators.bulk(tlds, validators.try_tld, "TLDs")
            params, body = {"domain": validators.domain(base_domain)}, {"tld": valid}
        else:
            raise validators.input_error(
                "Bulk Domain Availability has nothing to check",
                "Provide up to 100 Domains, or a Domain together with up to 100 TLDs",
            )
        if not valid:
            return outputs.bulk(None, None, skipped)
        result = self.connection.client.lookup(
            "Bulk Domain Availability", "POST", constants.PATH_DOMAIN_AVAILABILITY, params, body
        )
        return outputs.bulk(result, "bulk_domain_availability_response", skipped)
