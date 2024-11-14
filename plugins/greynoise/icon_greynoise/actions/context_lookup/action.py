import insightconnect_plugin_runtime
from .schema import ContextLookupInput, ContextLookupOutput, Input, Output, Component

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
        viz_base_url = "https://viz.greynoise.io/ip/"
        try:
            resp = self.connection.gn_client.ip(params.get(Input.IP_ADDRESS))
            if resp["seen"]:
                resp["first_seen"] = pendulum.parse(resp["first_seen"]).to_rfc3339_string()
                resp["last_seen"] = pendulum.parse(resp["last_seen"]).to_rfc3339_string()
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
            Output.ACTOR: resp.get("actor"),
            Output.BOT: resp.get("bot"),
            Output.CLASSIFICATION: resp.get("classification"),
            Output.CVE: resp.get("cve"),
            Output.FIRST_SEEN: resp.get("first_seen"),
            Output.IP: resp.get("ip"),
            Output.LAST_SEEN: resp.get("last_seen"),
            Output.METADATA: resp.get("metadata"),
            Output.RAW_DATA: resp.get("raw_data"),
            Output.SEEN: resp.get("seen"),
            Output.SPOOFABLE: resp.get("spoofable"),
            Output.TAGS: resp.get("tags"),
            Output.VIZ_URL: resp.get("viz_url"),
            Output.VPN: resp.get("vpn"),
            Output.VPN_SERVICE: resp.get("vpn_service"),
        }
