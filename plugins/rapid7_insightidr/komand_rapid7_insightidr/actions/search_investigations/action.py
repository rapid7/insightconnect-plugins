import insightconnect_plugin_runtime
from .schema import SearchInvestigationsInput, SearchInvestigationsOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from komand_rapid7_insightidr.util.endpoints import Investigations
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from komand_rapid7_insightidr.util.util import get_logging_context
import json
import datetime


class SearchInvestigations(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_investigations",
            description=Component.DESCRIPTION,
            input=SearchInvestigationsInput(),
            output=SearchInvestigationsOutput(),
        )

    def run(self, params={}):
        search = params.get(Input.SEARCH)
        sort = params.get(Input.SORT)
        start_time = (
            datetime.datetime.fromisoformat(params.get(Input.START_TIME))
            .astimezone(datetime.timezone.utc)
            .strftime("%Y-%m-%dT%H:%M:%SZ")
            if params.get(Input.START_TIME)
            else None
        )
        end_time = (
            datetime.datetime.fromisoformat(params.get(Input.END_TIME))
            .astimezone(datetime.timezone.utc)
            .strftime("%Y-%m-%dT%H:%M:%SZ")
            if params.get(Input.END_TIME)
            else None
        )
        size = params.get(Input.SIZE)
        index = params.get(Input.INDEX)

        data = clean(
            {
                Input.SEARCH: search,
                Input.SORT: sort,
                Input.START_TIME: start_time,
                Input.END_TIME: end_time,
            }
        )

        parameters = clean({Input.SIZE: size, Input.INDEX: index})

        self.connection.session.headers["Accept-version"] = "investigations-preview"
        request = ResourceHelper(self.connection.session, self.logger)

        endpoint = Investigations.search_investigation(self.connection.url)
        response = request.resource_request(endpoint, "post", payload=data, params=parameters)

        try:
            result = json.loads(response.get("resource"))
        except json.decoder.JSONDecodeError:
            self.logger.error(f"InsightIDR response: {response}", **get_logging_context())
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )
        try:
            investigations = clean(result.get("data", {}))
            metadata = result.get("metadata", {})
            return {Output.INVESTIGATIONS: investigations, Output.METADATA: metadata}
        except KeyError:
            self.logger.error(result, **get_logging_context())
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )
