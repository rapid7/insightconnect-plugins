import insightconnect_plugin_runtime
from .schema import ListTasksInput, ListTasksOutput, Input, Output, Component


class ListTasks(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_tasks",
            description=Component.DESCRIPTION,
            input=ListTasksInput(),
            output=ListTasksOutput(),
        )

    def run(self, params={}):
        offset = params.get(Input.OFFSET, "")
        limit = params.get(Input.LIMIT, "")
        endpoint = f"tasks/list"
        if offset and limit:
            endpoint = f"tasks/list/{limit}/{offset}"
        elif limit:
            endpoint = f"tasks/list/{limit}"
        response = self.connection.api.send(endpoint)
        return {Output.TASKS: response}
