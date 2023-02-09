import insightconnect_plugin_runtime
from .schema import AssignIncidentInput, AssignIncidentOutput

# Custom imports below


class AssignIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="assign_incident",
            description="Assign a person to an incident",
            input=AssignIncidentInput(),
            output=AssignIncidentOutput(),
        )

    def run(self, params={}):
        incident_id = params.get("incident_id")
        assignee = params.get("assignee")

        incident = self.connection.api.assign_incident(incident_id, assignee)

        return {"incident": incident}
