import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import BulkIpGeolocationInput, BulkIpGeolocationOutput, Input, Output, Component

# Custom imports below
from icon_whoisfreaks.util import constants, outputs, validators


class BulkIpGeolocation(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="bulk_ip_geolocation",
            description=Component.DESCRIPTION,
            input=BulkIpGeolocationInput(),
            output=BulkIpGeolocationOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        ip_addresses = params.get(Input.IP_ADDRESSES)
        # END INPUT BINDING - DO NOT REMOVE

        valid, skipped = validators.bulk(ip_addresses, validators.try_ip, "IP Addresses")
        if not valid:
            return outputs.bulk(None, None, skipped)
        result = self.connection.client.lookup(
            "Bulk IP Geolocation", "POST", constants.PATH_IP_GEOLOCATION, body={"ips": valid}
        )
        return outputs.bulk(result, None, skipped)
