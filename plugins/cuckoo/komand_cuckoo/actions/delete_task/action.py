import insightconnect_plugin_runtime
from .schema import DeleteTaskInput, DeleteTaskOutput, Input, Component
# Custom imports below
import requests


class DeleteTask(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_task",
            description=Component.DESCRIPTION,
            input=DeleteTaskInput(),
            output=DeleteTaskOutput(),
        )

    def run(self, params={}):
        task_id = params.get(Input.TASK_ID, "")
        endpoint = f"tasks/delete/{task_id}"

        response = requests.get(endpoint)
        response["message"] = "Task deleted"
        if response.get("status"):
            del response["status"]
        return response
