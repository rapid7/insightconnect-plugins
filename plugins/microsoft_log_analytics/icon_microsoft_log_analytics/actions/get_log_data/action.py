import insightconnect_plugin_runtime
from .schema import GetLogDataInput, GetLogDataOutput, Input, Component


class GetLogData(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_log_data", description=Component.DESCRIPTION, input=GetLogDataInput(), output=GetLogDataOutput()
        )

    def run(self, params={}):
        subscription_id = params.get(Input.SUBSCRIPTION_ID)
        resource_group_name = params.get(Input.RESOURCE_GROUP_NAME)
        workspace_name = params.get(Input.WORKSPACE_NAME)
        query = params.get(Input.QUERY)
        return self.connection.client.get_log_data(subscription_id, resource_group_name, workspace_name, query)
