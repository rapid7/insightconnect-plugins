import insightconnect_plugin_runtime
from .schema import ContextLookupInput, ContextLookupOutput, Input, Component

# Custom imports below
from icon_greynoise.util.util import GNRequestFailure, GNValueError
from greynoise.exceptions import RequestFailure
import pendulum


class ContextLookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="context_lookup",
            description=Component.DESCRIPTION,
            input=ContextLookupInput(),
            output=ContextLookupOutput(),
        )

    def run(self, params={}):
        try:
            resp = self.connection.gn_client.ip(params.get(Input.IP_ADDRESS))
            if resp["seen"]:
                resp["first_seen"] = pendulum.parse(resp["first_seen"]).to_rfc3339_string()
                resp["last_seen"] = pendulum.parse(resp["last_seen"]).to_rfc3339_string()
                resp["viz_url"] = "https://viz.greynoise.io/ip/" + str(params.get(Input.IP_ADDRESS))

        except RequestFailure as e:
            raise GNRequestFailure(e.args[0], e.args[1])
        except ValueError as e:
            raise GNValueError(e.args[0])

        return resp
