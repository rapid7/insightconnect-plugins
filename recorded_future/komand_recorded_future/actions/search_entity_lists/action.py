import insightconnect_plugin_runtime
from .schema import SearchEntityListsInput, SearchEntityListsOutput, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_recorded_future.util.api import Endpoint


class SearchEntityLists(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_entity_lists",
            description=Component.DESCRIPTION,
            input=SearchEntityListsInput(),
            output=SearchEntityListsOutput(),
        )

    def run(self, params={}):
        try:
            return {
                Output.ENTITIES: insightconnect_plugin_runtime.helper.clean(
                    self.connection.client.make_request(Endpoint.search_entity_lists(), params)
                    .get("data", {})
                    .get("results")
                )
            }
        except AttributeError as e:
            raise PluginException(
                cause="Recorded Future returned unexpected response.",
                assistance="Please check that the provided inputs are correct and try again.",
                data=e,
            )
