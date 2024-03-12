import insightconnect_plugin_runtime
from .schema import DeleteTaskInput, DeleteTaskOutput, Input

# Custom imports below
import json
import requests


class DeleteTask(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_task",
            description="Removes the given task from the database and deletes the results",
            input=DeleteTaskInput(),
            output=DeleteTaskOutput(),
        )

    def run(self, params={}):
        server = self.connection.server
        task_id = params.get(Input.TASK_ID, "")
        endpoint = f"{server}/tasks/delete/{task_id}"

        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            response = response.json()
            response["message"] = "Task deleted"
            del response["status"]
            return response

        except Exception as exception:
            self.logger.error(f"Error: {str(exception)}")
