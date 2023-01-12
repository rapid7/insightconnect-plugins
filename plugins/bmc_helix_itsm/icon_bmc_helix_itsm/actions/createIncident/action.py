import insightconnect_plugin_runtime
from .schema import CreateIncidentInput, CreateIncidentOutput, Input, Output, Component

# Custom imports below
from icon_bmc_helix_itsm.util.constants import IncidentRequest


class CreateIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="createIncident",
            description=Component.DESCRIPTION,
            input=CreateIncidentInput(),
            output=CreateIncidentOutput(),
        )

    def run(self, params={}):
        incident_parameters = {
            IncidentRequest.FIRST_NAME: params.get(Input.FIRSTNAME),
            IncidentRequest.LAST_NAME: params.get(Input.LASTNAME),
            IncidentRequest.DESCRIPTION: params.get(Input.DESCRIPTION),
            IncidentRequest.IMPACT: params.get(Input.IMPACT),
            IncidentRequest.URGENCY: params.get(Input.URGENCY),
            IncidentRequest.STATUS: params.get(Input.STATUS),
            IncidentRequest.REPORTED_SOURCE: params.get(Input.REPORTEDSOURCE),
            IncidentRequest.SERVICE_TYPE: params.get(Input.SERVICETYPE),
        }
        return {Output.INCIDENTNUMBER: self.connection.api_client.create_incident(incident_parameters)}
