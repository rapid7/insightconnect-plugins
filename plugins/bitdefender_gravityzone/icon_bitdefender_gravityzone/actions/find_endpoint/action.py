import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import FindEndpointInput, FindEndpointOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_bitdefender_gravityzone.util.helpers import (
    MIN_NAME_FILTER_LENGTH,
    find_exact_matches,
    get_short_label,
    normalize_hostname,
    to_endpoint_summary,
)


class FindEndpoint(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="find_endpoint",
            description=Component.DESCRIPTION,
            input=FindEndpointInput(),
            output=FindEndpointOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        hostname = params.get(Input.HOSTNAME)
        # END INPUT BINDING - DO NOT REMOVE

        target = normalize_hostname(hostname)
        short_label = get_short_label(target)
        if len(short_label) < MIN_NAME_FILTER_LENGTH:
            raise PluginException(
                cause=f"The hostname '{hostname}' is too short to search for in GravityZone.",
                assistance=f"Provide a hostname or FQDN whose part before the first dot has at least "
                f"{MIN_NAME_FILTER_LENGTH} characters. The GravityZone name filter needs {MIN_NAME_FILTER_LENGTH}.",
            )

        # The name filter is a prefix match, so the candidates are narrowed down to exact matches here
        candidates = self.connection.api.get_managed_endpoints_by_name(short_label)
        matches = find_exact_matches(candidates, target)
        self.logger.info(
            f"{len(candidates)} managed endpoints have a name starting with '{short_label}', "
            f"{len(matches)} of them match '{target}' exactly"
        )

        # Refuse to pick one when the hostname is ambiguous: acting on the wrong endpoint is worse than not acting
        if len(matches) != 1:
            return {Output.FOUND: False, Output.MATCH_COUNT: len(matches), Output.ENDPOINT: {}}
        return {Output.FOUND: True, Output.MATCH_COUNT: 1, Output.ENDPOINT: to_endpoint_summary(matches[0])}
