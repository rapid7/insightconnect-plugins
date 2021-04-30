import insightconnect_plugin_runtime
from .schema import GetTopClickersInput, GetTopClickersOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class GetTopClickers(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_top_clickers",
            description=Component.DESCRIPTION,
            input=GetTopClickersInput(),
            output=GetTopClickersOutput(),
        )

    def run(self, params={}):
        try:
            return {
                Output.RESULTS: insightconnect_plugin_runtime.helper.clean(
                    self.connection.client.get_top_clickers({"window": params.get(Input.WINDOW)})
                )
            }
        except AttributeError as e:
            raise PluginException(
                cause="Proofpoint Tap returned unexpected response.",
                assistance="Please check that the connection required for this action is set up and try again.",
                data=e,
            )
