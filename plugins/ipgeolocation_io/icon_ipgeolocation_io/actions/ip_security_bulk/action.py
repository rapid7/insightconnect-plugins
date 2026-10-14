import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import IpSecurityBulkInput, IpSecurityBulkOutput, Input, Output, Component

# Custom imports below
from icon_ipgeolocation_io.util.helpers import to_csv, validate_bulk_ips


class IpSecurityBulk(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="ip_security_bulk",
            description=Component.DESCRIPTION,
            input=IpSecurityBulkInput(),
            output=IpSecurityBulkOutput(),
        )

    @auto_instrument
    def run(self, params):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        excludes = params.get(Input.EXCLUDES)
        fields = params.get(Input.FIELDS)
        ips = params.get(Input.IPS)
        # END INPUT BINDING - DO NOT REMOVE

        # Domains are rejected up front, but bogon and private entries are left
        # in the payload so the API can report them per entry and the results
        # stay aligned with the submitted order.
        entries = validate_bulk_ips(ips, "IPs")

        query = {
            "fields": to_csv(fields),
            "excludes": to_csv(excludes),
        }

        results = self.connection.api.ip_security_bulk(entries, query)

        if not isinstance(results, list):
            raise PluginException(
                cause="IPGeolocation.io returned a single object instead of a list of bulk results.",
                assistance="Retry the action. If the problem persists, report it to the plugin maintainer.",
                data=str(results)[:1000],
            )

        self.logger.info(f"Received {len(results)} result(s) for {len(entries)} submitted IPs")

        return clean({Output.RESULTS: results})
