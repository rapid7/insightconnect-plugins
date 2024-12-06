import insightconnect_plugin_runtime
from .schema import RiotLookupInput, RiotLookupOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from greynoise.exceptions import RequestFailure


class RiotLookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="riot_lookup", description=Component.DESCRIPTION, input=RiotLookupInput(), output=RiotLookupOutput()
        )

    def run(self, params={}):
        try:
            viz_base_url = "https://viz.greynoise.io/ip/"
            resp = self.connection.gn_client.riot(params.get(Input.IP_ADDRESS))
            if resp["riot"]:
                resp.pop("logo_url", None)
                resp["viz_url"] = viz_base_url + str(resp["ip"])
        except RequestFailure as error:
            raise PluginException(
                cause=f"API responded with ERROR: {error.args[0]} - {error.args[1]}.",
                assistance="Please check error and try again.",
            )

        except ValueError as error:
            raise PluginException(
                cause=f"Input does not appear to be valid: {Input.IP_ADDRESS}. Error Message: {error.args[0]}",
                assistance="Please provide a valid public IPv4 address.",
            )

        return {
            Output.IP: resp.get("ip"),
            Output.RIOT: resp.get("riot"),
            Output.DESCRIPTION: resp.get("description"),
            Output.VIZ_URL: resp.get("viz_url"),
            Output.NAME: resp.get("name"),
            Output.CATEGORY: resp.get("category"),
            Output.EXPLANATION: resp.get("explanation"),
            Output.LAST_UPDATED: resp.get("last_updated"),
            Output.REFERENCE: resp.get("reference"),
            Output.TRUST_LEVEL: resp.get("trust_level"),
        }
