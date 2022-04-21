import insightconnect_plugin_runtime

from .schema import QueryIndicatorInput, QueryIndicatorOutput, Input, Output, Component
from icon_azure_sentinel.util.tools import map_output_for_list


class QueryIndicator(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="query_indicator",
            description=Component.DESCRIPTION,
            input=QueryIndicatorInput(),
            output=QueryIndicatorOutput(),
        )

    def run(self, params={}):
        subscription_id = params.pop(Input.SUBSCRIPTIONID)
        resource_group_name = params.pop(Input.RESOURCEGROUPNAME)
        workspace_name = params.pop(Input.WORKSPACENAME)
        data_dict = self.connection.api_client.query_indicator(
            resource_group_name, workspace_name, subscription_id, **params
        )
        values = map_output_for_list(data_dict.get("value"))

        return {Output.INDICATORS: values}
