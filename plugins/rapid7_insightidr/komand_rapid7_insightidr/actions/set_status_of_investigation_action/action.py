import insightconnect_plugin_runtime
from .schema import (
    SetStatusOfInvestigationActionInput,
    SetStatusOfInvestigationActionOutput,
    Component,
    Input,
    Output,
)
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Investigations
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
import json


class SetStatusOfInvestigationAction(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="set_status_of_investigation_action",
            description=Component.DESCRIPTION,
            input=SetStatusOfInvestigationActionInput(),
            output=SetStatusOfInvestigationActionOutput(),
        )

    def run(self, params={}):
        idr_id = params.get(Input.ID)
        status = params.get(Input.STATUS)

        self.connection.headers["Accept-version"] = "investigations-preview"
        request = ResourceHelper(self.connection.headers, self.logger)

        endpoint = Investigations.set_the_status_of_an_investigation(self.connection.url, idr_id, status)
        response = request.resource_request(endpoint, "put")

        try:
            result = json.loads(response["resource"])
        except json.decoder.JSONDecodeError:
            self.logger.error(f"InsightIDR response: {response}", **self.connection.cloud_log_values)
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )
        try:
            return {Output.INVESTIGATION: clean(result)}
        except KeyError:
            self.logger.error(result, **self.connection.cloud_log_values)
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )
