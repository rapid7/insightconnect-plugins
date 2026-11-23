import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import IpGeolocationBulkInput, IpGeolocationBulkOutput, Input, Output, Component

# Custom imports below
from icon_ipgeolocation_io.util.constants import INCLUDE_MODULES_IPGEO
from icon_ipgeolocation_io.util.helpers import (
    normalize_choices,
    normalize_language,
    to_csv,
    validate_bulk_entries,
)


class IpGeolocationBulk(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="ip_geolocation_bulk",
            description=Component.DESCRIPTION,
            input=IpGeolocationBulkInput(),
            output=IpGeolocationBulkOutput(),
        )

    @auto_instrument
    def run(self, params):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        excludes = params.get(Input.EXCLUDES)
        fields = params.get(Input.FIELDS)
        include = params.get(Input.INCLUDE)
        ips = params.get(Input.IPS)
        lang = params.get(Input.LANG)
        # END INPUT BINDING - DO NOT REMOVE

        # Entries are kept in the submitted order because the API returns one
        # result per entry positionally. Domains are allowed alongside IPs.
        entries = validate_bulk_entries(ips, "IPs or Domains")

        query = {
            "include": normalize_choices(include, INCLUDE_MODULES_IPGEO, "Include"),
            "fields": to_csv(fields),
            "excludes": to_csv(excludes),
            "lang": normalize_language(lang),
        }

        results = self.connection.api.ip_geolocation_bulk(entries, query)

        if not isinstance(results, list):
            raise PluginException(
                cause="IPGeolocation.io returned a single object instead of a list of bulk results.",
                assistance="Retry the action. If the problem persists, report it to the plugin maintainer.",
                data=str(results)[:1000],
            )

        self.logger.info(f"Received {len(results)} result(s) for {len(entries)} submitted entries")

        return clean({Output.RESULTS: results})
