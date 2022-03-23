import insightconnect_plugin_runtime

from .schema import GetIndicatorInput, GetIndicatorOutput, Input, Component


class GetIndicator(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_indicator",
            description=Component.DESCRIPTION,
            input=GetIndicatorInput(),
            output=GetIndicatorOutput(),
        )

    def run(self, params={}):
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)
        indicator_name = params.get(Input.NAME)
        data_dict = self.connection.api_client.get_indicator(
            resource_group_name, workspace_name, subscription_id, indicator_name
        )

        return data_dict
