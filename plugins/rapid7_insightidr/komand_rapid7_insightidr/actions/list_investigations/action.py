import insightconnect_plugin_runtime

from .schema import ListInvestigationsInput, ListInvestigationsOutput, Component, Output, Input
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Investigations
from komand_rapid7_insightidr.util.resource_helper import (
    ResourceHelper,
    get_sort_param,
    get_priorities_param,
    get_sources_param,
)
import json
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
        rest_params = {}
        start_time = params.get(Input.START_TIME)
        end_time = params.get(Input.END_TIME)
        email = params.get(Input.EMAIL)
        sort = params.get(Input.SORT)
        priorities = params.get(Input.PRIORITIES)
        sources = params.get(Input.SOURCES)

        for key in params:
            if params[key]:
                rest_params[key] = params[key]
        if not rest_params.get("statuses"):
            raise PluginException(
                cause="The statuses parameter cannot be blank.",
                assistance="choose a statues parameter, and please report this bug to support.",
            )
        if rest_params.get("statuses") == "EITHER":
            del rest_params["statuses"]

        if start_time:
            start_time_parsed = datetime.datetime.fromisoformat(start_time)
            rest_params["start_time"] = start_time_parsed.astimezone(datetime.timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            )
        if end_time:
            end_time_parsed = datetime.datetime.fromisoformat(end_time)
            rest_params["end_time"] = end_time_parsed.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

        if email:
            rest_params["assignee.email"] = email

        if sort:
            rest_params[Input.SORT] = get_sort_param(sort)

        if priorities:
            rest_params[Input.PRIORITIES] = get_priorities_param(priorities)

        if sources:
            rest_params[Input.SOURCES] = get_sources_param(sources)

        request = ResourceHelper(self.connection.session, self.logger)

        endpoint = Investigations.list_investigations(self.connection.url)
        response = request.make_request(endpoint, "GET", params=rest_params)

        investigations = clean(response.get("data", {}))
        metadata = response.get("metadata", {})
        return {Output.INVESTIGATIONS: investigations, Output.METADATA: metadata}
