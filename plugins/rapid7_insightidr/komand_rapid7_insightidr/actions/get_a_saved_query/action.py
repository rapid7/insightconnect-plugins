import insightconnect_plugin_runtime

from .schema import GetASavedQueryInput, GetASavedQueryOutput, Input, Output, Component
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from komand_rapid7_insightidr.util.endpoints import Queries
from insightconnect_plugin_runtime.exceptions import PluginException
from validators import uuid
import json


class GetASavedQuery(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_a_saved_query",
            description=Component.DESCRIPTION,
            input=GetASavedQueryInput(),
            output=GetASavedQueryOutput(),
        )

    def run(self, params={}):
        query_id = params.get(Input.QUERY_ID)
        if not uuid(query_id):
            raise PluginException(
                cause="Query ID field did not contain a valid UUID.",
                assistance="Please enter a valid UUID value in the Query ID field.",
                data=f"Query ID: {query_id}",
            )
        self.connection.headers["Accept-version"] = "investigations-preview"
        request = ResourceHelper(self.connection.headers, self.logger)
        response = request.resource_request(Queries.get_query_by_id(self.connection.region, query_id), "get")
        try:
            result = json.loads(response["resource"])
            saved_query = insightconnect_plugin_runtime.helper.clean(result.get("saved_query"))
        except json.decoder.JSONDecodeError:
            self.logger.error(f"InsightIDR response: {response}", **self.connection.cloud_log_values)
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
                data=response,
            )
        return {Output.SAVED_QUERY: saved_query}
