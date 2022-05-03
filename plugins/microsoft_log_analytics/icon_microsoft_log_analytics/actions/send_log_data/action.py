import insightconnect_plugin_runtime
from .schema import SendLogDataInput, SendLogDataOutput, Input, Output, Component

# Custom imports below


class SendLogData(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="send_log_data",
            description=Component.DESCRIPTION,
            input=SendLogDataInput(),
            output=SendLogDataOutput(),
        )

    def run(self, params={}):
        subscription_id = params.get(Input.SUBSCRIPTION_ID)
        resource_group_name = params.get(Input.RESOURCE_GROUP_NAME)
        workspace_name = params.get(Input.WORKSPACE_NAME)
        log_type = params.get(Input.LOG_TYPE, "")
        log_data = params.get(Input.LOG_DATA, [])
        self.connection.client.send_log_data(subscription_id, resource_group_name, workspace_name, log_type, log_data)
        return {Output.MESSAGE: "Log data has been added", Output.LOG_DATA: params.get(Input.LOG_DATA, [])}
