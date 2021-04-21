import insightconnect_plugin_runtime
from .schema import RiotLookupInput, RiotLookupOutput, Input, Component

# Custom imports below
from greynoise.exceptions import RequestFailure
from insightconnect_plugin_runtime.exceptions import PluginException


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
