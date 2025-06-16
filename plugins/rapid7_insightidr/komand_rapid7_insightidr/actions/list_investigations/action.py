import insightconnect_plugin_runtime

from .schema import ListInvestigationsInput, ListInvestigationsOutput, Component, Output, Input
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Investigations
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper, get_sort_param, convert_list_to_string
import datetime


class ListInvestigations(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_investigations",
            description=Component.DESCRIPTION,
            input=ListInvestigationsInput(),
            output=ListInvestigationsOutput(),
        )

    def run(self, params={}):
        start_time = params.get(Input.START_TIME)
        end_time = params.get(Input.END_TIME)

        rest_params = {
            "assignee.email": params.get(Input.EMAIL),
            "sources": convert_list_to_string(params.get(Input.SOURCES)),
            "sort": get_sort_param(params.get(Input.SORT)),
            "priorities": convert_list_to_string(params.get(Input.PRIORITIES)),
            "statuses": convert_list_to_string(params.get(Input.STATUSES)),
            "size": params.get(Input.SIZE),
            "index": params.get(Input.INDEX),
        }

        if start_time:
            start_time_parsed = datetime.datetime.fromisoformat(start_time)
            rest_params["start_time"] = start_time_parsed.astimezone(datetime.timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            )
        if end_time:
            end_time_parsed = datetime.datetime.fromisoformat(end_time)
            rest_params["end_time"] = end_time_parsed.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        rest_params = clean(rest_params)

        request = ResourceHelper(self.connection.headers, self.logger)

        endpoint = Investigations.list_investigations(self.connection.url)
        response = request.make_request(endpoint, "GET", params=rest_params)

        investigations = clean(response.get("data", {}))
        metadata = response.get("metadata", {})
        return {Output.INVESTIGATIONS: investigations, Output.METADATA: metadata}
