import insightconnect_plugin_runtime

from .schema import AppendTagsInput, AppendTagsOutput, Input, Component


class AppendTags(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="append_tags", description=Component.DESCRIPTION, input=AppendTagsInput(), output=AppendTagsOutput()
        )

    def run(self, params={}):
        subscription_id = params.pop(Input.SUBSCRIPTIONID)
        resource_group_name = params.pop(Input.RESOURCEGROUPNAME)
        workspace_name = params.pop(Input.WORKSPACENAME)
        indicator_name = params.pop(Input.NAME)
        data_dict = self.connection.api_client.append_tags(
            resource_group_name, workspace_name, subscription_id, indicator_name, **params
        )

        return data_dict
