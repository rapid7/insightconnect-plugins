import insightconnect_plugin_runtime
from .schema import GetIncidentByNumberInput, GetIncidentByNumberOutput, Input, Output, Component

# Custom imports below


class GetIncidentByNumber(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="getIncidentByNumber",
            description=Component.DESCRIPTION,
            input=GetIncidentByNumberInput(),
            output=GetIncidentByNumberOutput(),
        )

    def run(self, params={}):
        incident_number = params.get(Input.INCIDENTNUMBER)
        self.logger.info(f"Getting information about incident with Number={incident_number}\n")
        incident = self.connection.api_client.get_incident_by_number(incident_number)
        self.logger.info(f"Incident result: {incident}\n")
        return {Output.INCIDENT: incident}
