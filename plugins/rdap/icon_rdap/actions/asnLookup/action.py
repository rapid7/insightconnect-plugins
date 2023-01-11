import insightconnect_plugin_runtime
from .schema import AsnLookupInput, AsnLookupOutput, Input, Output, Component
from icon_rdap.util.api import RdapAPI
from icon_rdap.util.helpers import convert_keys_to_camel


class AsnLookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="asnLookup", description=Component.DESCRIPTION, input=AsnLookupInput(), output=AsnLookupOutput()
        )

    def run(self, params={}) -> dict:
        asn = params.get(Input.ASN)
        self.logger.info(f"[ACTION LOG] Getting information for ASN number: {asn}\n")

        asn_result = RdapAPI(logger=self.logger).asn_lookup(asn=asn)
        self.logger.info(f"[ACTION LOG] ASN result: {asn_result}\n")

        return {Output.RESULTS: convert_keys_to_camel(asn_result)}
