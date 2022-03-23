import insightconnect_plugin_runtime

from .schema import CreateIndicatorInput, CreateIndicatorOutput, Input, Component


class CreateIndicator(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_indicator",
            description=Component.DESCRIPTION,
            input=CreateIndicatorInput(),
            output=CreateIndicatorOutput(),
        )

    def run(self, params={}):
        subscription_id = params.pop(Input.SUBSCRIPTIONID)
        resource_group_name = params.pop(Input.RESOURCEGROUPNAME)
        workspace_name = params.pop(Input.WORKSPACENAME)
        data_dict = self.connection.api_client.create_indicator(
            resource_group_name, workspace_name, subscription_id, **params
        )

        return data_dict
