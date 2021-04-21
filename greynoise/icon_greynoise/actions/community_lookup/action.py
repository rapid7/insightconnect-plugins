import insightconnect_plugin_runtime
from .schema import CommunityLookupInput, CommunityLookupOutput, Input, Component

# Custom imports below
from greynoise import GreyNoise
from greynoise.exceptions import RequestFailure
from insightconnect_plugin_runtime.exceptions import PluginException
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
