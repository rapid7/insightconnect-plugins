import insightconnect_plugin_runtime
from .schema import CommunityLookupInput, CommunityLookupOutput, Input, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from greynoise.exceptions import RequestFailure
from greynoise import GreyNoise
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
        gn_client = GreyNoise(
            api_server=self.connection.server,
            api_key=self.connection.api_key,
            integration_name=self.connection.user_agent,
            offering="community",
        )
        try:
            resp = gn_client.ip(params.get(Input.IP_ADDRESS))
            if resp["noise"] or resp["riot"]:
                resp["last_seen"] = pendulum.parse(resp["last_seen"]).to_rfc3339_string()

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

        return resp
