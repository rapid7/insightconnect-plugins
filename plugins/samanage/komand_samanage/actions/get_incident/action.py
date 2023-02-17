import insightconnect_plugin_runtime
from .schema import GetIncidentInput, GetIncidentOutput

# Custom imports below


class GetIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_incident",
            description="Get incident details",
            input=GetIncidentInput(),
            output=GetIncidentOutput(),
        )

    def run(self, params={}):
        incident_id = params.get("incident_id")
        incident = self.connection.api.get_incident(incident_id)
        return {"incident": incident}
