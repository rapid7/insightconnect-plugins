import insightconnect_plugin_runtime
from .schema import QuickLookupInput, QuickLookupOutput, Input, Output, Component

# Custom imports below
from greynoise.exceptions import RequestFailure
from insightconnect_plugin_runtime.exceptions import PluginException


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
                cause="Received HTTP %d status code from GreyNoise. Verify your input and try again." % e.args[0],
                assistance="If the issue persists please contact support.",
                data=f"{e.args[0]}, {e.args[1]['message']}",
            )
        except ValueError as e:
            raise PluginException(
                cause="Received HTTP 404 status code from GreyNoise. "
                "Input provided was not found, please try another.",
                assistance="If the issue persists please contact support.",
                data=f"{e.args[0]}",
            )

        return resp_out
