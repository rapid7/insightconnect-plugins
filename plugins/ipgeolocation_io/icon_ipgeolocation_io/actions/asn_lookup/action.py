import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import AsnLookupInput, AsnLookupOutput, Input, Output, Component

# Custom imports below
from icon_ipgeolocation_io.util.constants import INCLUDE_MODULES_ASN
from icon_ipgeolocation_io.util.helpers import normalize_asn, normalize_choices, to_csv, validate_ip


class AsnLookup(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="asn_lookup", description=Component.DESCRIPTION, input=AsnLookupInput(), output=AsnLookupOutput()
        )

    @auto_instrument
    def run(self, params):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        asn = params.get(Input.ASN)
        excludes = params.get(Input.EXCLUDES)
        fields = params.get(Input.FIELDS)
        include = params.get(Input.INCLUDE)
        ip = params.get(Input.IP)
        # END INPUT BINDING - DO NOT REMOVE

        query = {
            "include": normalize_choices(include, INCLUDE_MODULES_ASN, "Include"),
            "fields": to_csv(fields),
            "excludes": to_csv(excludes),
        }

        # With neither, the API resolves the orchestrator's own public IP.
        address = validate_ip(ip, "IP")
        if address:
            query["ip"] = address
        if normalize_asn(asn):
            query["asn"] = normalize_asn(asn)

        response = self.connection.api.asn_lookup(query)

        # The ip key comes back only when the lookup was performed by IP, so it
        # is dropped from the output rather than returned as null.
        return clean(
            {
                Output.IP: response.get("ip"),
                Output.ASN: response.get("asn", {}),
            }
        )
