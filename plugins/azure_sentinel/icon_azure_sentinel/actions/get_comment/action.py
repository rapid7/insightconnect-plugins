import insightconnect_plugin_runtime
from .schema import GetCommentInput, GetCommentOutput, Input, Output, Component


class GetComment(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_comment", description=Component.DESCRIPTION, input=GetCommentInput(), output=GetCommentOutput()
        )

    def run(self, params={}):
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        incident_comment_id = params.get(Input.INCIDENTCOMMENTID)
        incident_id = params.get(Input.INCIDENTID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)
        comment = self.connection.api_client.get_comment(
            incident_id, incident_comment_id, resource_group_name, workspace_name, subscription_id
        )
        return {Output.COMMENT: comment}
