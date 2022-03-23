import insightconnect_plugin_runtime

from .schema import DeleteIndicatorInput, DeleteIndicatorOutput, Input, Output, Component


class DeleteIndicator(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_indicator",
            description=Component.DESCRIPTION,
            input=DeleteIndicatorInput(),
            output=DeleteIndicatorOutput(),
        )

    def run(self, params={}):
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)
        indicator_name = params.get(Input.NAME)
        self.connection.api_client.delete_indicator(
            resource_group_name, workspace_name, subscription_id, indicator_name
        )
        return {Output.MESSAGE: f"Indicator name: {indicator_name} deleted"}
