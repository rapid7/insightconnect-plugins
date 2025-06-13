import insightconnect_plugin_runtime
from .schema import SetPriorityOfInvestigationInput, SetPriorityOfInvestigationOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from komand_rapid7_insightidr.util.endpoints import Investigations
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from komand_rapid7_insightidr.util.util import get_logging_context

# Custom imports below
import json


class SetPriorityOfInvestigation(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="set_priority_of_investigation",
            description=Component.DESCRIPTION,
            input=SetPriorityOfInvestigationInput(),
            output=SetPriorityOfInvestigationOutput(),
        )

    def run(self, params={}):
        identifier = params.get(Input.ID)
        priority = params.get(Input.PRIORITY)

        self.connection.session.headers["Accept-version"] = "investigations-preview"
        request = ResourceHelper(self.connection.session, self.logger)

        endpoint = Investigations.set_the_priority_of_an_investigation(self.connection.url, identifier, priority)
        response = request.resource_request(endpoint, "put")

        try:
            result = json.loads(response["resource"])
        except json.decoder.JSONDecodeError:
            self.logger.error(f"InsightIDR response: {response}", **self.connection.log_values)
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )
        try:
            return {Output.INVESTIGATION: clean(result)}
        except KeyError:
            self.logger.error(result, **self.connection.log_values)
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )
