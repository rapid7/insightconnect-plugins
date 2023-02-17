import insightconnect_plugin_runtime
from .schema import GetCommentsInput, GetCommentsOutput

# Custom imports below


class GetComments(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_comments",
            description="Get all comments of an incident",
            input=GetCommentsInput(),
            output=GetCommentsOutput(),
        )

    def run(self, params={}):
        incident_id = params.get("incident_id")

        comments = self.connection.api.get_comments(incident_id)

        return {"comments": comments}
