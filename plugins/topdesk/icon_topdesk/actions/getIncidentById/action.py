import insightconnect_plugin_runtime
from .schema import GetIncidentByIdInput, GetIncidentByIdOutput, Input, Output, Component

# Custom imports below


class GetIncidentById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="getIncidentById",
            description=Component.DESCRIPTION,
            input=GetIncidentByIdInput(),
            output=GetIncidentByIdOutput(),
        )

    def run(self, params={}):
        incident_id = params.get(Input.ID)
        self.logger.info(f"Getting information about incident with ID={incident_id}\n")
        incident = self.connection.api_client.get_incident_by_id(incident_id)
        self.logger.info(f"Incident result: {incident}\n")
        return {Output.INCIDENT: incident}
