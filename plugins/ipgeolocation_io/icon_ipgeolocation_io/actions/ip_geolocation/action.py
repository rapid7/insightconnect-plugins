import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import IpGeolocationInput, IpGeolocationOutput, Input, Output, Component

# Custom imports below
from icon_ipgeolocation_io.util.constants import INCLUDE_MODULES_IPGEO
from icon_ipgeolocation_io.util.helpers import clean_string, normalize_choices, normalize_language, to_csv


class IpGeolocation(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="ip_geolocation",
            description=Component.DESCRIPTION,
            input=IpGeolocationInput(),
            output=IpGeolocationOutput(),
        )

    @auto_instrument
    def run(self, params):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        excludes = params.get(Input.EXCLUDES)
        fields = params.get(Input.FIELDS)
        include = params.get(Input.INCLUDE)
        ip = params.get(Input.IP)
        lang = params.get(Input.LANG)
        user_agent = params.get(Input.USER_AGENT)
        # END INPUT BINDING - DO NOT REMOVE

        # An IP is optional here. Omitting it asks the API to geolocate the
        # orchestrator's own public IP, and the value may also be a domain.
        query = {
            "ip": clean_string(ip),
            "include": normalize_choices(include, INCLUDE_MODULES_IPGEO, "Include"),
            "fields": to_csv(fields),
            "excludes": to_csv(excludes),
            "lang": normalize_language(lang),
        }

        # The API parses whatever arrives in the User-Agent header, so a caller
        # supplied string is forwarded as a header rather than a query value.
        result = self.connection.api.ip_geolocation(query, user_agent=clean_string(user_agent))

        return clean({Output.RESULT: result})
