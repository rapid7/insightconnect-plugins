import insightconnect_plugin_runtime
from .schema import ListTasksInput, ListTasksOutput, Input, Output

# Custom imports below
import requests


class ListTasks(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_tasks",
            description="Returns list of tasks",
            input=ListTasksInput(),
            output=ListTasksOutput(),
        )

    def run(self, params={}):
        server = self.connection.server
        offset = params.get(Input.OFFSET, "")
        limit = params.get(Input.LIMIT, "")

        if offset:
            if limit:
                endpoint = f"{server}/tasks/list/{limit}/{offset}"
            else:
                endpoint = f"{server}/tasks/list"
        elif limit:
            endpoint = f"{server}/tasks/list/{limit}"
        else:
            endpoint = f"{server}/tasks/list"

        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            response = response.json()
            return {Output.TASKS: response}

        except Exception as exception:
            self.logger.error(f"Error: {str(exception)}")
