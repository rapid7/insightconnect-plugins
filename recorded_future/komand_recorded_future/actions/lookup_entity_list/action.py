import insightconnect_plugin_runtime
from .schema import LookupEntityListInput, LookupEntityListOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_recorded_future.util.api import Endpoint


class LookupEntityList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="lookup_entity_list",
            description=Component.DESCRIPTION,
            input=LookupEntityListInput(),
            output=LookupEntityListOutput(),
        )

    def run(self, params={}):
        try:
            return {
                Output.ENTITIES: insightconnect_plugin_runtime.helper.clean(
                    self.connection.client.make_request(Endpoint.lookup_entity_list(params.get(Input.ENTITY_LIST_ID)))
                    .get("data")
                    .get("results")
                )
            }
        except AttributeError as e:
            raise PluginException(
                cause="Recorded Future returned unexpected response.",
                assistance="Please check that the provided input is correct and try again.",
                data=e,
            )
