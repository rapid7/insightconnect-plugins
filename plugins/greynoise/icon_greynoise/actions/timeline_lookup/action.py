import insightconnect_plugin_runtime
from .schema import TimelineLookupInput, TimelineLookupOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from greynoise.exceptions import RateLimitError, RequestFailure
from greynoise.util import validate_ip


class TimelineLookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="timeline_lookup",
            description=Component.DESCRIPTION,
            input=TimelineLookupInput(),
            output=TimelineLookupOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        ip_address = params.get(Input.IP_ADDRESS)
        days = params.get(Input.DAYS)
        # END INPUT BINDING - DO NOT REMOVE

        try:
            validate_ip(ip_address)
            resp = self.connection.gn_client.timelinedaily(ip_address, days=days or 7)

        except RateLimitError as error:
            raise PluginException(
                cause="GreyNoise API rate limit exceeded.",
                assistance="Wait and try again.",
                data=str(error),
            )

        except RequestFailure as error:
            raise PluginException(
                cause=f"API responded with ERROR: {error.args[0]} - {error.args[1]}.",
                assistance="Please check error and try again.",
            )

        except ValueError as error:
            raise PluginException(
                cause=f"Input does not appear to be valid: {ip_address}. Error Message: {error.args[0]}",
                assistance="Please provide a valid IPv4 Address.",
            )

        metadata = resp.get("metadata") if isinstance(resp, dict) else None
        data = resp.get("data") if isinstance(resp, dict) and isinstance(resp.get("data"), list) else []
        output = {Output.IP: ip_address, Output.DATA: data}
        if isinstance(metadata, dict):
            output[Output.METADATA] = metadata
            if metadata.get("ip"):
                output[Output.IP] = metadata.get("ip")
        return output
