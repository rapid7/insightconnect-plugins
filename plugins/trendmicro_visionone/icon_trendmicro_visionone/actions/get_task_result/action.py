import insightconnect_plugin_runtime
from .schema import GetTaskResultInput, GetTaskResultOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class GetTaskResult(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_task_result",
            description=Component.DESCRIPTION,
            input=GetTaskResultInput(),
            output=GetTaskResultOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        task_id = params.get(Input.TASK_ID)
        poll = params.get(Input.POLL)
        poll_time_sec = params.get(Input.POLL_TIME_SEC)
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.get_base_task_result(
            task_id=task_id,
            poll=poll,
            poll_time_sec=poll_time_sec,
        )
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while retrieving the task result.",
                assistance="Please check the task ID and try again.",
                data=response,
            )
        # Return results
        self.logger.info("Returning Results...")
        return {
            Output.ACTION: response.response.dict().get("action", ""),
            Output.ACCOUNT: response.response.dict().get("account", ""),
            Output.CREATED_DATE_TIME: response.response.dict().get("created_date_time", ""),
            Output.AGENT_GUID: response.response.dict().get("agent_guid", ""),
            Output.ID: response.response.dict().get("id", ""),
            Output.LAST_ACTION_DATE_TIME: response.response.dict().get("last_action_date_time", ""),
            Output.RESOURCE_LOCATION: response.response.dict().get("resource_location", ""),
            Output.STATUS: response.response.dict().get("status", ""),
            Output.DESCRIPTION: response.response.dict().get("description", ""),
            Output.ENDPOINT_NAME: response.response.dict().get("endpoint_name", ""),
            Output.EXPIRED_DATE_TIME: response.response.dict().get("expired_date_time", ""),
            Output.FILE_PATH: response.response.dict().get("file_path", ""),
            Output.FILE_SHA1: response.response.dict().get("file_sha1", ""),
            Output.FILE_SHA256: response.response.dict().get("file_sha256", ""),
            Output.FILE_SIZE: response.response.dict().get("file_size", 0),
            Output.FILENAME: response.response.dict().get("filename", ""),
            Output.IMAGE_PATH: response.response.dict().get("image_path", ""),
            Output.PASSWORD: response.response.dict().get("password", ""),
            Output.PID: response.response.dict().get("pid", 0),
            Output.SANDBOX_TASK_ID: response.response.dict().get("sandbox_task_id", ""),
            Output.TASKS: response.response.dict().get("tasks", []),
            Output.URL: response.response.dict().get("url", ""),
        }
