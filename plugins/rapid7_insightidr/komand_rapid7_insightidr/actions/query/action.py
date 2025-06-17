import insightconnect_plugin_runtime
from .schema import QueryInput, QueryOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightidr.util.endpoints import QueryLogs
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from komand_rapid7_insightidr.util.formatting import refactor_message
from komand_rapid7_insightidr.util.constants import THREE_MONTHS_SECONDS, TWENTY_FOURTH_NOVEMBER
import json
import time


class Query(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="query",
            description=Component.DESCRIPTION,
            input=QueryInput(),
            output=QueryOutput(),
        )

    def run(self, params={}):
        most_recent_first = params.get(Input.MOST_RECENT_FIRST)
        time_now = int(time.time())
        self.connection.headers["Accept-version"] = "investigations-preview"
        request = ResourceHelper(self.connection.headers, self.logger)
        from_var = time_now - THREE_MONTHS_SECONDS
        if most_recent_first and from_var < TWENTY_FOURTH_NOVEMBER:
            from_var = TWENTY_FOURTH_NOVEMBER

        request_params = {"from": from_var * 1000, "to": time_now * 1000, "most_recent_first": most_recent_first}
        response = request.resource_request(
            QueryLogs.get_query_logs(self.connection.region, params.get(Input.ID)), "get", params=request_params
        )

        try:
            result = json.loads(response["resource"])
            if response["status"] == 202:
                response = request.resource_request(result["links"][0]["href"], "get", params=request_params)
                result = json.loads(response["resource"])
        except (json.decoder.JSONDecodeError, IndexError, KeyError):
            self.logger.error(f"InsightIDR response: {response}")
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details.",
            )

        try:
            result_response = []
            events = result.get("events", [])
            if events:
                for event in events:
                    event["message"] = refactor_message(event["message"])
                    result_response.append(event)

            return {Output.EVENTS: result_response}
        except KeyError:
            self.logger.error(result)
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details.",
            )
