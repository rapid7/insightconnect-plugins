import insightconnect_plugin_runtime
from .schema import CommunityLookupInput, CommunityLookupOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from greynoise.exceptions import RateLimitError, RequestFailure
from greynoise.util import validate_ip
import pendulum


class CommunityLookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="community_lookup",
            description=Component.DESCRIPTION,
            input=CommunityLookupInput(),
            output=CommunityLookupOutput(),
        )

    def run(self, params={}):
        ip_address = params.get(Input.IP_ADDRESS)
        try:
            validate_ip(ip_address)
            resp = self.connection.gn_client.request(f"v3/community/{ip_address}")
            if not isinstance(resp, dict):
                raise PluginException(
                    cause="GreyNoise Community API returned an unexpected response.",
                    assistance="Please check the IP address and try again.",
                )
            if (resp.get("noise") or resp.get("riot")) and resp.get("last_seen"):
                resp["last_seen"] = pendulum.parse(resp["last_seen"]).to_rfc3339_string()

        except RateLimitError as error:
            raise PluginException(
                cause="GreyNoise API rate limit exceeded.",
                assistance="Wait and try again.",
                data=str(error),
            )

        except RequestFailure as error:
            raise PluginException(
                cause=f"API responded with ERROR: {error.args[0]} - {error.args[1]}.",
                assistance="Please check error and try again.",
            )

        except ValueError as error:
            raise PluginException(
                cause=f"Input does not appear to be valid: {ip_address}. Error Message: {error.args[0]}",
                assistance="Please provide a valid public IPv4 address.",
            )

        return {
            Output.CLASSIFICATION: resp.get("classification"),
            Output.IP: resp.get("ip"),
            Output.LAST_SEEN: resp.get("last_seen"),
            Output.LINK: resp.get("link"),
            Output.MESSAGE: resp.get("message"),
            Output.NAME: resp.get("name"),
            Output.NOISE: resp.get("noise"),
            Output.RIOT: resp.get("riot"),
        }
