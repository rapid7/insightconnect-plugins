import insightconnect_plugin_runtime
from .schema import QuickLookupInput, QuickLookupOutput, Input, Component

# Custom imports below
from icon_greynoise.util.util import GNRequestFailure, GNValueError
from greynoise.exceptions import RequestFailure


class QuickLookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="quick_lookup", description=Component.DESCRIPTION, input=QuickLookupInput(), output=QuickLookupOutput()
        )

    def run(self, params={}):
        try:
            resp = self.connection.gn_client.quick(params.get(Input.IP_ADDRESS))
            if resp:
                resp_out = resp[0]
            else:
                resp_out = {"ip": params.get(Input.IP_ADDRESS), "code": "0x07", "code_message": "Input Not A Valid IP"}

        except RequestFailure as e:
            raise PluginException(
                cause=f"API responded with ERROR: {e.args[0]} - {e.args[1]}.",
                assistance="Please check error and try again.",
            )

        except ValueError as e:
            raise PluginException(
                cause=f"Input does not appear to be valid: {Input.IP_ADDRESS}. Error Message: {e.args[0]}",
                assistance="Please provide a valid public IPv4 address.",
            )

        return resp_out
