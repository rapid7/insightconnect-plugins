import insightconnect_plugin_runtime
from .schema import AsnLookupInput, AsnLookupOutput, Input, Output, Component
from icon_rdap.util.helpers import return_non_empty, parse_entities


class AsnLookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="asnLookup", description=Component.DESCRIPTION, input=AsnLookupInput(), output=AsnLookupOutput()
        )

    def run(self, params={}) -> dict:
        asn = params.get(Input.ASN)

        self.logger.info(f"[ACTION LOG] Getting information for ASN number: {asn}")
        asn_result = self.connection.rdap_client.asn_lookup(asn=asn)
        self.logger.info(f"[ACTION LOG] ASN result: {asn_result}\n")

        return return_non_empty(
            {
                Output.HANDLE: asn_result.get("handle"),
                Output.STARTAUTNUM: asn_result.get("startAutnum"),
                Output.ENDAUTNUM: asn_result.get("endAutnum"),
                Output.NAME: asn_result.get("name"),
                Output.TYPE: asn_result.get("type"),
                Output.COUNTRY: asn_result.get("country"),
                Output.EVENTS: asn_result.get("events"),
                Output.ENTITIES: parse_entities(asn_result.get("entities")),
                Output.PORT43: asn_result.get("port43"),
                Output.STATUS: asn_result.get("status"),
            }
        )
