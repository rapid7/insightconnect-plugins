import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import IpGeolocationInput, IpGeolocationOutput, Input, Output, Component

# Custom imports below
from icon_whoisfreaks.util import constants, outputs, validators


class IpGeolocation(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="ip_geolocation",
            description=Component.DESCRIPTION,
            input=IpGeolocationInput(),
            output=IpGeolocationOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        ip_address = params.get(Input.IP_ADDRESS)
        # END INPUT BINDING - DO NOT REMOVE

        ip_value, reason = validators.ip(ip_address)
        if reason:
            return outputs.not_looked_up(reason)
        result = self.connection.client.lookup("IP Geolocation", "GET", constants.PATH_IP_GEOLOCATION, {"ip": ip_value})
        location = outputs.get_path(result.data_dict, "location")
        return outputs.single(
            result,
            {
                Output.COUNTRY_CODE: outputs.to_str(outputs.get_path(location, "country_code2")),
                Output.COUNTRY_NAME: outputs.to_str(outputs.get_path(location, "country_name")),
                Output.CITY: outputs.to_str(outputs.get_path(location, "city")),
            },
        )
