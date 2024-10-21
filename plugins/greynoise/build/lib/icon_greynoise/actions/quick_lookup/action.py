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
            raise GNRequestFailure(e.args[0], e.args[1])
        except ValueError as e:
            raise GNValueError(e.args[0])

        return resp_out
