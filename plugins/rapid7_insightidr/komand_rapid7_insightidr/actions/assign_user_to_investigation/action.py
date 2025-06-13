import insightconnect_plugin_runtime
from .schema import (
    AssignUserToInvestigationInput,
    AssignUserToInvestigationOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
import json
from insightconnect_plugin_runtime.helper import clean
from komand_rapid7_insightidr.util.endpoints import Investigations
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from komand_rapid7_insightidr.util.util import get_logging_context


class AssignUserToInvestigation(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="assign_user_to_investigation",
            description=Component.DESCRIPTION,
            input=AssignUserToInvestigationInput(),
            output=AssignUserToInvestigationOutput(),
        )

    def run(self, params={}):
        investigation_id = params.get(Input.ID)
        user_email = params.get(Input.USER_EMAIL_ADDRESS)

        payload = {"user_email_address": user_email}

        self.connection.session.headers["Accept-version"] = "investigations-preview"
        request = ResourceHelper(self.connection.session, self.logger)

        endpoint = Investigations.set_user_for_investigation(self.connection.url, investigation_id)
        response = request.resource_request(endpoint, "put", payload=payload)

        try:
            result = json.loads(response.get("resource"))
        except json.decoder.JSONDecodeError:
            self.logger.error(f"InsightIDR response: {response}", **self.connection.log_values)
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )
        try:
            return {Output.SUCCESS: True, Output.INVESTIGATION: clean(result)}
        except KeyError:
            self.logger.error(result, **self.connection.log_values)
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )
