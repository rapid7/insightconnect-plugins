import insightconnect_plugin_runtime
from .schema import TimelineLookupInput, TimelineLookupOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from greynoise.exceptions import RequestFailure


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
        # END INPUT BINDING - DO NOT REMOVE

        try:
            resp = self.connection.gn_client.timelinedaily(ip_address)

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
        breakpoint()
        return {Output.IP: resp.get("ip"), Output.ACTIVITY: resp.get("activity"), Output.METADATA: resp.get("metadata")}
