import insightconnect_plugin_runtime
from .schema import CreateIncidentInput, CreateIncidentOutput, Input, Output, Component

# Custom imports below
from icon_topdesk.util.helpers import prepare_incident_payload
from icon_topdesk.util.constants import INCIDENT_STATUS
from insightconnect_plugin_runtime.exceptions import PluginException


class CreateIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="createIncident",
            description=Component.DESCRIPTION,
            input=CreateIncidentInput(),
            output=CreateIncidentOutput(),
        )

    def run(self, params={}):
        # Check if no caller or callerLookup parameters provided
        if params.get(Input.CALLER, {}) == {} and params.get(Input.CALLERLOOKUP, "") == "":
            raise PluginException(
                cause="No caller or caller lookup provided",
                assistance="One of these inputs must be supplied to create an incident.\nThe caller parameter is automatically filled in when the caller lookup parameter is provided.",
            )

        parameters = prepare_incident_payload(params.copy())
        self.logger.info(f"Creating an incident with the following parameters: \n{parameters}\n")

        if parameters.get("status", ""):
            parameters["status"] = INCIDENT_STATUS.get(params.get(Input.STATUS))

        return {Output.INCIDENT: self.connection.api_client.create_incident(parameters)}
