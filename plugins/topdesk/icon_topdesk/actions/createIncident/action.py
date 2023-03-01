import insightconnect_plugin_runtime
from .schema import CreateIncidentInput, CreateIncidentOutput, Input, Output, Component

# Custom imports below
from icon_topdesk.util.helpers import prepare_incident_payload
from icon_topdesk.util.constants import INCIDENT_STATUS


class CreateIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="createIncident",
            description=Component.DESCRIPTION,
            input=CreateIncidentInput(),
            output=CreateIncidentOutput(),
        )

    def run(self, params={}):
        parameters = prepare_incident_payload(params.copy())
        parameters["status"] = INCIDENT_STATUS.get(params.get(Input.STATUS))
        self.logger.info(f"Creating an incident with the following parameters: \n{parameters}\n")
        return {Output.INCIDENT: self.connection.api_client.create_incident(parameters)}
