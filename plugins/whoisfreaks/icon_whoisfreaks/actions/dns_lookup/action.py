import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import DnsLookupInput, DnsLookupOutput, Input, Output, Component

# Custom imports below
from icon_whoisfreaks.util import constants, outputs, validators


class DnsLookup(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="dns_lookup",
            description=Component.DESCRIPTION,
            input=DnsLookupInput(),
            output=DnsLookupOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        cname_depth = params.get(Input.CNAME_DEPTH)
        domain = params.get(Input.DOMAIN)
        ip_address = params.get(Input.IP_ADDRESS)
        record_types = params.get(Input.RECORD_TYPES)
        relative_records = params.get(Input.RELATIVE_RECORDS)
        # END INPUT BINDING - DO NOT REMOVE

        domain_value = validators.optional_text(domain)
        ip_value = validators.optional_text(ip_address)
        if not domain_value and not ip_value:
            raise validators.input_error(
                "DNS Lookup needs a Domain or an IP Address", "Provide Domain, IP Address, or both"
            )
        params = {
            "type": validators.record_types(record_types),
            "cnameDepth": validators.integer(cname_depth, "CNAME Depth", 0, 4),
            "relativeRecords": relative_records if isinstance(relative_records, bool) else None,
        }
        if domain_value:
            params["domainName"] = validators.domain(domain_value)
        if ip_value:
            params["ipAddress"], reason = validators.ip(ip_value)
            if reason and not domain_value:
                return outputs.not_looked_up(reason)
        result = self.connection.client.lookup("DNS Lookup", "GET", constants.PATH_LIVE_DNS, params)
        return outputs.single(result, {Output.RECORDS: outputs.to_object_list(result.data_dict.get("dnsRecords"))})
