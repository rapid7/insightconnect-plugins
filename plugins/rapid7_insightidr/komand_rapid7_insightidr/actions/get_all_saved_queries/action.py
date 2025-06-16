import insightconnect_plugin_runtime
from .schema import GetAllSavedQueriesInput, GetAllSavedQueriesOutput, Input, Output, Component
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from komand_rapid7_insightidr.util.endpoints import Queries
from insightconnect_plugin_runtime.exceptions import PluginException
import json


class GetAllSavedQueries(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_all_saved_queries",
            description=Component.DESCRIPTION,
            input=GetAllSavedQueriesInput(),
            output=GetAllSavedQueriesOutput(),
        )

    def run(self):
        self.connection.headers["Accept-version"] = "investigations-preview"
        request = ResourceHelper(self.connection.headers, self.logger)
        response = request.resource_request(Queries.get_all_queries(self.connection.region), "get")
        try:
            result = json.loads(response["resource"])
            saved_queries = insightconnect_plugin_runtime.helper.clean(result.get("saved_queries"))
        except json.decoder.JSONDecodeError:
            self.logger.error(f"InsightIDR response: {response}", **self.connection.cloud_log_values)
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
                data=response,
            )
        return {Output.SAVED_QUERIES: saved_queries}
