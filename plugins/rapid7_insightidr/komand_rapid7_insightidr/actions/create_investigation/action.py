import insightconnect_plugin_runtime
from .schema import CreateInvestigationInput, CreateInvestigationOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from komand_rapid7_insightidr.util.endpoints import Investigations
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper

# Custom imports below
import json


class CreateInvestigation(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_investigation",
            description=Component.DESCRIPTION,
            input=CreateInvestigationInput(),
            output=CreateInvestigationOutput(),
        )

    def run(self, params={}):
        title = params.get(Input.TITLE)
        status = params.get(Input.STATUS)
        priority = params.get(Input.PRIORITY)
        disposition = params.get(Input.DISPOSITION)
        email = params.get(Input.EMAIL)

        data = clean(
            {
                Input.TITLE: title,
                Input.STATUS: status,
                Input.PRIORITY: priority,
                Input.DISPOSITION: disposition,
            }
        )

        if email:
            data.update({"assignee": {Input.EMAIL: email}})

        self.connection.headers["Accept-version"] = "investigations-preview"
        request = ResourceHelper(self.connection.headers, self.logger)

        endpoint = Investigations.create_investigation(self.connection.url)
        response = request.resource_request(endpoint, "post", payload=data)

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
