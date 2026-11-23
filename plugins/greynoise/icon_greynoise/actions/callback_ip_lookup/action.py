import insightconnect_plugin_runtime
from .schema import CallbackIpLookupInput, CallbackIpLookupOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from greynoise.exceptions import RateLimitError, RequestFailure


class CallbackIpLookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="callback_ip_lookup",
            description=Component.DESCRIPTION,
            input=CallbackIpLookupInput(),
            output=CallbackIpLookupOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        ip_address = params.get(Input.IP_ADDRESS)
        source_workspace = params.get(Input.SOURCE_WORKSPACE) or "all"
        # END INPUT BINDING - DO NOT REMOVE

        try:
            resp = self.connection.gn_client.callback_ip(ip_address, source_workspace=source_workspace)

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
                assistance="Please provide a valid public IPv4 address.",
            )

        if not isinstance(resp, dict):
            resp = {}

        output = {
            Output.IP: resp.get("ip"),
            Output.SOURCE_WORKSPACES: resp.get("source_workspaces"),
            Output.IS_STAGE_1: resp.get("is_stage_1"),
            Output.IS_STAGE_2: resp.get("is_stage_2"),
            Output.FIRST_SEEN: resp.get("first_seen"),
            Output.LAST_SEEN: resp.get("last_seen"),
            Output.SCANNER_IPS: resp.get("scanner_ips"),
            Output.SCANNER_COUNT: resp.get("scanner_count"),
            Output.FILE_COUNT: resp.get("file_count"),
            Output.ACTIVE_FILES: resp.get("active_files"),
            Output.MESSAGE: resp.get("message"),
        }
        return {key: value for key, value in output.items() if value is not None}
