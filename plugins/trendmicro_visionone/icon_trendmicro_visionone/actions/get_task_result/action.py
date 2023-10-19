import insightconnect_plugin_runtime

from .schema import GetTaskResultInput, GetTaskResultOutput, Input, Output, Component
from icon_trendmicro_visionone.util.constants import RESPONSE_MAPPING
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
        # Make first API Call to get the action type
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
        action = response.response.dict().get("action", "")
        action_type = RESPONSE_MAPPING.get(action.value)
        # Make second API Call to get the action result
        response = client.get_task_result(
            task_id=task_id,
            class_=action_type,
            poll=poll,
            poll_time_sec=poll_time_sec,
        )
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while retrieving the task result.",
                assistance="Please check the task ID and try again.",
                data=response,
            )
        # Avoid None values
        response_dict = response.response.dict()
        for key, value in response_dict.items():
            if value is None and key in ["file_size", "pid"]:
                response_dict[key] = 0
            elif value is None:
                response_dict[key] = "None"
        # Return results
        self.logger.info("Returning Results...")
        return {
            Output.ACTION: response_dict.get("action", ""),
            Output.ACCOUNT: response_dict.get("account", ""),
            Output.CREATED_DATE_TIME: response_dict.get("created_date_time", ""),
            Output.AGENT_GUID: response_dict.get("agent_guid", ""),
            Output.ID: response_dict.get("id", ""),
            Output.LAST_ACTION_DATE_TIME: response_dict.get(
                "last_action_date_time", ""
            ),
            Output.RESOURCE_LOCATION: response_dict.get("resource_location", ""),
            Output.STATUS: response_dict.get("status", ""),
            Output.DESCRIPTION: response_dict.get("description", ""),
            Output.ENDPOINT_NAME: response_dict.get("endpoint_name", ""),
            Output.EXPIRED_DATE_TIME: response_dict.get("expired_date_time", ""),
            Output.FILE_PATH: response_dict.get("file_path", ""),
            Output.FILE_SHA1: response_dict.get("file_sha1", ""),
            Output.FILE_SHA256: response_dict.get("file_sha256", ""),
            Output.FILE_SIZE: response_dict.get("file_size", 0),
            Output.FILENAME: response_dict.get("filename", ""),
            Output.IMAGE_PATH: response_dict.get("image_path", ""),
            Output.PASSWORD: response_dict.get("password", ""),
            Output.PID: response_dict.get("pid", 0),
            Output.SANDBOX_TASK_ID: response_dict.get("sandbox_task_id", ""),
            Output.TASKS: response_dict.get("tasks", []),
            Output.URL: response_dict.get("url", ""),
        }
