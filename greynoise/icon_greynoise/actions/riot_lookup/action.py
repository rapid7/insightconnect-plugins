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
            raise GNRequestFailure(e.args[0], e.args[1])
        except ValueError as e:
            raise GNValueError(e.args[0])

        return resp
