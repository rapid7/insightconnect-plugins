import insightconnect_plugin_runtime

from .schema import ReplaceTagsInput, ReplaceTagsOutput, Input, Component


class ReplaceTags(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="replace_tags", description=Component.DESCRIPTION, input=ReplaceTagsInput(), output=ReplaceTagsOutput()
        )

    def run(self, params={}):
        subscription_id = params.pop(Input.SUBSCRIPTIONID)
        resource_group_name = params.pop(Input.RESOURCEGROUPNAME)
        workspace_name = params.pop(Input.WORKSPACENAME)
        indicator_name = params.pop(Input.NAME)
        data_dict = self.connection.api_client.replace_tags(
            resource_group_name, workspace_name, subscription_id, indicator_name, **params
        )

        return data_dict
