import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import SslLookupInput, SslLookupOutput, Input, Output, Component

# Custom imports below
from icon_whoisfreaks.util import constants, outputs, validators


class SslLookup(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="ssl_lookup",
            description=Component.DESCRIPTION,
            input=SslLookupInput(),
            output=SslLookupOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        domain = params.get(Input.DOMAIN)
        include_chain = params.get(Input.INCLUDE_CHAIN)
        include_raw = params.get(Input.INCLUDE_RAW)
        # END INPUT BINDING - DO NOT REMOVE

        params = {"domainName": validators.domain(domain), "chain": bool(include_chain), "sslRaw": bool(include_raw)}
        result = self.connection.client.lookup("SSL Lookup", "GET", constants.PATH_SSL, params)
        certificates = outputs.to_object_list(result.data_dict.get("sslCertificates"))
        leaf = certificates[0] if certificates else {}
        return outputs.single(
            result,
            {
                Output.CERTIFICATES: certificates or None,
                Output.VALID_FROM: outputs.to_str(leaf.get("validityStartDate")),
                Output.VALID_TO: outputs.to_str(leaf.get("validityEndDate")),
            },
        )
