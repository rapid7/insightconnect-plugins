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
from icon_rapid7_insightidr.util.endpoints import Investigations
from insightconnect_plugin_runtime.exceptions import PluginException


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

        endpoint = Investigations.set_user_for_investigation(self.connection.url, investigation_id)
        payload = {"user_email_address": user_email}

        response = self.connection.session.put(endpoint, json=payload)
        try:
            response.raise_for_status()
        except Exception as e:
            raise PluginException(
                cause="The IDR API returned an error.",
                assistance="Usually this is the result of an invalid user email or investigation ID. Please see the following for more information:\n",
                data=response.text,
            )

        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            self.logger.error(f"InsightIDR response: {response}")
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
                data=response,
            )

        return {Output.SUCCESS: True, Output.INVESTIGATION: result}
