import insightconnect_plugin_runtime
from .schema import GetInvestigationInput, GetInvestigationOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from komand_rapid7_insightidr.util.endpoints import Investigations
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper

# Custom imports below
import json


class GetInvestigation(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_investigation",
            description=Component.DESCRIPTION,
            input=GetInvestigationInput(),
            output=GetInvestigationOutput(),
        )

    def run(self, params={}):
        identifier = params.get(Input.ID)
        self.connection.headers["Accept-version"] = "investigations-preview"
        request = ResourceHelper(self.connection.headers, self.logger)

        endpoint = Investigations.update_or_get_investigation(self.connection.url, identifier)
        response = request.resource_request(endpoint, "get")

        try:
            result = json.loads(response.get("resource"))
        except json.decoder.JSONDecodeError:
            self.logger.error(f"InsightIDR response: {response}", **request.logging_context)
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )
        try:
            return {Output.INVESTIGATION: clean(result)}
        except KeyError:
            self.logger.error(result, **request.logging_context)
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )
