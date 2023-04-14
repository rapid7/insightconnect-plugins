import insightconnect_plugin_runtime
from .schema import AttachIncidentInput, AttachIncidentOutput

# Custom imports below


class AttachIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="attach_incident",
            description="Attach a file to an incident",
            input=AttachIncidentInput(),
            output=AttachIncidentOutput(),
        )

    def run(self, params={}):
        incident_id = params.get("incident_id")
        attachment_bytes = params.get("attachment_bytes")
        attachment_name = params.get("attachment_name")

        attachment = self.connection.api.attach_file_to_incident(incident_id, attachment_bytes, attachment_name)

        return {"attachment": attachment}
