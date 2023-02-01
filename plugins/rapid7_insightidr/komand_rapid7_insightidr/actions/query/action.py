import insightconnect_plugin_runtime
from .schema import QueryInput, QueryOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightidr.util.endpoints import QueryLogs
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
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
        request = ResourceHelper(self.connection.session, self.logger)
        # 7776000 - is for three months from now.
        # It is here because InsightDR keep logs for three months in hot storage
        three_months_seconds = 7776000
        # The way data indexing works changed on the 24/11/2022.
        # For any search with most_recent_first=true 'from' must not be older than 24/11/2022
        twenty_fourth_november = 1669248000
        if (time_now - three_months_seconds) > twenty_fourth_november:
            from_var = (time_now - three_months_seconds)
        else:
            from_var = twenty_fourth_november
        request_params = {"from": from_var * 1000, "to": time_now * 1000,
                          "most_recent_first": most_recent_first}
        response = request.resource_request(
            QueryLogs.get_query_logs(self.connection.region, params.get(Input.ID)),
            "get",
            params=request_params
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
                assistance="Contact support for help. See log for more details."
            )

        try:
            result_response = []
            events = result.get("events", [])
            if events:
                for event in events:
                    print(json.loads(event["message"].replace("\n", "\\n")))
                    # event["message"] = json.loads(event["message"].replace("\n", "\\n"))
                    event["message"] = json.loads(json.dumps(event["message"]).replace("\n", "\\n"))
                    result_response.append(event)

            return {Output.EVENTS: result_response}
        except KeyError:
            self.logger.error(result)
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details."
            )
