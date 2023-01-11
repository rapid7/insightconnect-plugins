import insightconnect_plugin_runtime
from .schema import IpLookupInput, IpLookupOutput, Input, Output, Component
from icon_rdap.util.api import RdapAPI
from icon_rdap.util.helpers import convert_keys_to_camel, extract_asn_result
from icon_rdap.util.ipwhois_lookup import IPWhoisLookup


class IpLookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="ipLookup", description=Component.DESCRIPTION, input=IpLookupInput(), output=IpLookupOutput()
        )

    def run(self, params={}) -> dict:
        ip_input = params.get(Input.IPADDRESS)
        include_asn = params.get(Input.GETASN)
        self.logger.info(f"[ACTION LOG] Getting information for IP address: {ip_input}. Include ASN: {include_asn}.\n")

        ip_result = RdapAPI(logger=self.logger).ip_lookup(ip_input)

        if include_asn:
            ipwhois_rdap_result = IPWhoisLookup(logger=self.logger).perform_lookup_rdap(ip_address=ip_input)
            ip_result.update(extract_asn_result(ipwhois_rdap_result))
            self.logger.info("[ACTION LOG] IP result updated with ASN.\n")

        self.logger.info(f"[ACTION LOG] IP result: {ip_result}\n")
        return {Output.RESULTS: convert_keys_to_camel(ip_result)}
