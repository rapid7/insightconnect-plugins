import insightconnect_plugin_runtime
from .schema import ListCommentsInput, ListCommentsOutput, Input, Output, Component


class ListComments(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_comments",
            description=Component.DESCRIPTION,
            input=ListCommentsInput(),
            output=ListCommentsOutput(),
        )

    def run(self, params={}):
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        incident_id = params.get(Input.INCIDENTID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)
        entities = self.connection.api_client.list_comments(
            incident_id, resource_group_name, workspace_name, subscription_id
        )
        return {Output.COMMENTS: entities}
