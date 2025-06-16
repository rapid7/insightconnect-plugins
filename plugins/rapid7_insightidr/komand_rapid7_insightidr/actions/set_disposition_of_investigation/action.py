import insightconnect_plugin_runtime
from .schema import SetDispositionOfInvestigationInput, SetDispositionOfInvestigationOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from komand_rapid7_insightidr.util.endpoints import Investigations
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper

# Custom imports below
import json


class SetDispositionOfInvestigation(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="set_disposition_of_investigation",
            description=Component.DESCRIPTION,
            input=SetDispositionOfInvestigationInput(),
            output=SetDispositionOfInvestigationOutput(),
        )

    def run(self, params={}):
        identifier = params.get(Input.ID)
        disposition = params.get(Input.DISPOSITION)

        self.connection.headers["Accept-version"] = "investigations-preview"
        request = ResourceHelper(self.connection.headers, self.logger)

        endpoint = Investigations.set_the_disposition_of_an_investigation(self.connection.url, identifier, disposition)
        response = request.resource_request(endpoint, "put")

        try:
            result = json.loads(response.get("resource"))
        except json.decoder.JSONDecodeError:
            self.logger.error(f"InsightIDR response: {response}")
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )
        try:
            return {Output.INVESTIGATION: clean(result)}
        except KeyError:
            self.logger.error(result)
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )
