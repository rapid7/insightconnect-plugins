import insightconnect_plugin_runtime
from .schema import IpLookupInput, IpLookupOutput, Input, Output, Component
from icon_rdap.util.helpers import extract_asn_result, parse_entities, return_non_empty
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
        ip_result = self.connection.rdap_client.ip_lookup(ip_input)

        if include_asn:
            ipwhois_rdap_result = IPWhoisLookup(logger=self.logger).perform_lookup_rdap(ip_address=ip_input)
            ip_result.update(extract_asn_result(ipwhois_rdap_result))
            self.logger.info("[ACTION LOG] IP result updated with ASN.\n")
        ip_result["entities"] = parse_entities(ip_result.get("entities", []))

        return return_non_empty(
            {
                Output.ASN: ip_result.get("asn"),
                Output.ASNCIDR: ip_result.get("asn_cidr"),
                Output.ANSCOUNTRYCODE: ip_result.get("asn_country_code", ""),
                Output.ASNDATE: ip_result.get("asn_date"),
                Output.ASNDESCRIPTION: ip_result.get("asn_description"),
                Output.ANSREGISTRY: ip_result.get("asn_registry", ""),
                Output.HANDLE: ip_result.get("handle"),
                Output.STARTADDRESS: ip_result.get("startAddress"),
                Output.ENDADDRESS: ip_result.get("endAddress"),
                Output.IPVERSION: ip_result.get("ipVersion"),
                Output.NAME: ip_result.get("name"),
                Output.TYPE: ip_result.get("type"),
                Output.COUNTRY: ip_result.get("country"),
                Output.PARENTHANDLE: ip_result.get("parentHandle"),
                Output.ENTITIES: ip_result.get("entities"),
                Output.EVENTS: ip_result.get("events"),
                Output.PORT43: ip_result.get("port43"),
                Output.STATUS: ip_result.get("status"),
            }
        )
