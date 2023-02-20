import insightconnect_plugin_runtime
from .schema import CommentIncidentInput, CommentIncidentOutput

# Custom imports below


class CommentIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="comment_incident",
            description="Add a comment to an incident",
            input=CommentIncidentInput(),
            output=CommentIncidentOutput(),
        )

    def run(self, params={}):
        incident_id = params.get("incident_id")
        body = params.get("body")
        is_private = params.get("is_private")
        comment = self.connection.api.comment_incident(incident_id, body, is_private)
        return {"comment": comment}
