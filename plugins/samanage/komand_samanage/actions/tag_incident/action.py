import insightconnect_plugin_runtime
from .schema import TagIncidentInput, TagIncidentOutput

# Custom imports below


class TagIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="tag_incident",
            description="Add tags to an incident",
            input=TagIncidentInput(),
            output=TagIncidentOutput(),
        )

    def run(self, params={}):
        incident_id = params.get("incident_id")
        tags = params.get("tags")

        incident = self.connection.api.add_tags_to_incident(incident_id, tags)

        return {"incident": incident}
