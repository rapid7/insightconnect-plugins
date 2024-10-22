import insightconnect_plugin_runtime
from .schema import ContextLookupInput, ContextLookupOutput, Input, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
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
            raise PluginException(
                cause=f"API responded with ERROR: {e.args[0]} - {e.args[1]}.",
                assistance="Please check error and try again.",
            )

        except ValueError as e:
            raise PluginException(
                cause=f"Input does not appear to be valid: {Input.IP_ADDRESS}. Error Message: {e.args[0]}",
                assistance="Please provide a valid public IPv4 address.",
            )

        return resp
