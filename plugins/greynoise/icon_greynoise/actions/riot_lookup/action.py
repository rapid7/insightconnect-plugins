import insightconnect_plugin_runtime
from .schema import RiotLookupInput, RiotLookupOutput, Input, Component

# Custom imports below
from icon_greynoise.util.util import GNRequestFailure, GNValueError
from greynoise.exceptions import RequestFailure


class RiotLookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="riot_lookup", description=Component.DESCRIPTION, input=RiotLookupInput(), output=RiotLookupOutput()
        )

    def run(self, params={}):
        try:
            resp = self.connection.gn_client.riot(params.get(Input.IP_ADDRESS))
            if resp["riot"]:
                resp.pop("logo_url", None)
                resp["viz_url"] = "https://viz.greynoise.io/riot/" + str(params.get(Input.IP_ADDRESS))
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
