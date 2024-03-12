import insightconnect_plugin_runtime
from .schema import ListMemoryInput, ListMemoryOutput, Input

# Custom imports below
import requests


class ListMemory(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_memory",
            description="Returns a list of memory dump files or one memory dump file associated with the specified task ID",
            input=ListMemoryInput(),
            output=ListMemoryOutput(),
        )

    def run(self, params={}):
        server = self.connection.server
        task_id = params.get(Input.TASK_ID, "")
        endpoint = f"{server}/memory/list/{task_id}"

        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            response = response.json()
            return response

        except Exception as exception:
            self.logger.error(f"Error: {str(exception)}")
