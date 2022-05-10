import insightconnect_plugin_runtime
from .schema import DeleteCommentInput, DeleteCommentOutput, Input, Output, Component

# Custom imports below


class DeleteComment(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_comment",
            description=Component.DESCRIPTION,
            input=DeleteCommentInput(),
            output=DeleteCommentOutput(),
        )

    def run(self, params={}):
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        incident_comment_id = params.get(Input.INCIDENTCOMMENTID)
        incident_id = params.get(Input.INCIDENTID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)
        status_code = self.connection.api_client.delete_comment(
            incident_id, incident_comment_id, resource_group_name, workspace_name, subscription_id
        )
        return {Output.STATUS: status_code}
