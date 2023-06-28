import insightconnect_plugin_runtime
from .schema import GetTopClickersInput, GetTopClickersOutput, Input, Output, Component

# Custom imports below
from komand_proofpoint_tap.util.helpers import clean


class GetTopClickers(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_top_clickers",
            description=Component.DESCRIPTION,
            input=GetTopClickersInput(),
            output=GetTopClickersOutput(),
        )

    def run(self, params={}):
        self.connection.client.check_authorization()
        results = clean(self.connection.client.get_top_clickers({"window": params.get(Input.WINDOW)}))
        return {
            Output.USERS: results.get("users", []),
            Output.TOTALTOPCLICKERS: results.get("totalTopClickers", 0),
            Output.INTERVAL: results.get("interval", ""),
        }
