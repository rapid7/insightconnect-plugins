import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import AsnWhoisInput, AsnWhoisOutput, Input, Output, Component

# Custom imports below
from icon_whoisfreaks.util import constants, outputs, validators


class AsnWhois(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="asn_whois",
            description=Component.DESCRIPTION,
            input=AsnWhoisInput(),
            output=AsnWhoisOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        asn = params.get(Input.ASN)
        # END INPUT BINDING - DO NOT REMOVE

        result = self.connection.client.lookup(
            "ASN WHOIS", "GET", constants.PATH_ASN_WHOIS, {"asn": validators.asn(asn)}
        )
        data = result.data_dict
        return outputs.single(
            result,
            {
                Output.AS_NAME: outputs.to_str(data.get("asName")),
                Output.ORGANIZATION_NAME: outputs.to_str(data.get("orgName")),
                Output.COUNTRY: outputs.to_str(data.get("country")),
            },
        )
