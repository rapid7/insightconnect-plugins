import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import AbuseContactInput, AbuseContactOutput, Input, Output, Component

# Custom imports below
from icon_ipgeolocation_io.util.helpers import to_csv, validate_ip


class AbuseContact(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="abuse_contact",
            description=Component.DESCRIPTION,
            input=AbuseContactInput(),
            output=AbuseContactOutput(),
        )

    @auto_instrument
    def run(self, params):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        excludes = params.get(Input.EXCLUDES)
        fields = params.get(Input.FIELDS)
        ip = params.get(Input.IP)
        # END INPUT BINDING - DO NOT REMOVE

        address = validate_ip(ip, "IP")
        if not address:
            raise PluginException(
                cause="No IP address was provided.",
                assistance="Provide the IPv4 or IPv6 address to find the responsible abuse contact for.",
            )

        query = {
            "ip": address,
            "fields": to_csv(fields),
            "excludes": to_csv(excludes),
        }

        response = self.connection.api.abuse_contact(query)

        return clean(
            {
                Output.IP: response.get("ip", address),
                Output.ABUSE: response.get("abuse", {}),
            }
        )
