import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import IpSecurityInput, IpSecurityOutput, Input, Output, Component

# Custom imports below
from icon_ipgeolocation_io.util.helpers import to_csv, validate_ip


class IpSecurity(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="ip_security", description=Component.DESCRIPTION, input=IpSecurityInput(), output=IpSecurityOutput()
        )

    @auto_instrument
    def run(self, params):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        excludes = params.get(Input.EXCLUDES)
        fields = params.get(Input.FIELDS)
        ip = params.get(Input.IP)
        # END INPUT BINDING - DO NOT REMOVE

        # /v3/security rejects domains with an opaque 401 and bogons with a 423,
        # so both are caught here to give the operator a usable message instead.
        query = {
            "ip": validate_ip(ip, "IP"),
            "fields": to_csv(fields),
            "excludes": to_csv(excludes),
        }

        response = self.connection.api.ip_security(query)

        return clean(
            {
                Output.IP: response.get("ip"),
                Output.SECURITY: response.get("security", {}),
            }
        )
