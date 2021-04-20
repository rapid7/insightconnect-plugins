import insightconnect_plugin_runtime
from .schema import ContextLookupInput, ContextLookupOutput, Input, Output, Component

# Custom imports below
from greynoise.exceptions import RequestFailure
from insightconnect_plugin_runtime.exceptions import PluginException
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

        return resp
