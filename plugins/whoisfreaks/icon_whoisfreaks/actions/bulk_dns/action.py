import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import BulkDnsInput, BulkDnsOutput, Input, Output, Component

# Custom imports below
from icon_whoisfreaks.util import constants, outputs, validators


class BulkDns(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="bulk_dns",
            description=Component.DESCRIPTION,
            input=BulkDnsInput(),
            output=BulkDnsOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        cname_depth = params.get(Input.CNAME_DEPTH)
        domains = params.get(Input.DOMAINS)
        ip_addresses = params.get(Input.IP_ADDRESSES)
        record_types = params.get(Input.RECORD_TYPES)
        # END INPUT BINDING - DO NOT REMOVE

        if not domains and not ip_addresses:
            raise validators.input_error(
                "Bulk DNS needs Domains or IP Addresses", "Provide up to 100 values in either list"
            )
        valid_domains, skipped_domains = validators.bulk(domains, validators.try_domain, "Domains", required=False)
        valid_ips, skipped_ips = validators.bulk(ip_addresses, validators.try_ip, "IP Addresses", required=False)
        skipped = skipped_domains + skipped_ips
        if not valid_domains and not valid_ips:
            return outputs.bulk(None, None, skipped)
        params = {
            "type": validators.record_types(record_types),
            "cname_depth": validators.integer(cname_depth, "CNAME Depth", 0, 4),
        }
        body = {key: value for key, value in (("domainNames", valid_domains), ("ipAddresses", valid_ips)) if value}
        result = self.connection.client.lookup("Bulk DNS", "POST", constants.PATH_BULK_DNS, params, body)
        return outputs.bulk(result, "bulk_dns_info", skipped)
