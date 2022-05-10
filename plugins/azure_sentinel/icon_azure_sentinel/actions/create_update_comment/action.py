import insightconnect_plugin_runtime
from .schema import CreateUpdateCommentInput, CreateUpdateCommentOutput, Input, Output, Component


class CreateUpdateComment(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_update_comment",
            description=Component.DESCRIPTION,
            input=CreateUpdateCommentInput(),
            output=CreateUpdateCommentOutput(),
        )

    def run(self, params={}):
        subscription_id = params.pop(Input.SUBSCRIPTIONID)
        incident_id = params.pop(Input.INCIDENTID)
        resource_group_name = params.pop(Input.RESOURCEGROUPNAME)
        workspace_name = params.pop(Input.WORKSPACENAME)
        incident_comment_id = params.pop(Input.INCIDENTCOMMENTID)

        data_dict = self.connection.api_client.create_update_comment(
            incident_id, incident_comment_id, resource_group_name, workspace_name, subscription_id, **params
        )
        return data_dict
