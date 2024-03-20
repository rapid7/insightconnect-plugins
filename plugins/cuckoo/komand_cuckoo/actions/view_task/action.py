import insightconnect_plugin_runtime
from .schema import ViewTaskInput, ViewTaskOutput, Input, Component, Output


class ViewTask(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="view_task",
            description=Component.DESCRIPTION,
            input=ViewTaskInput(),
            output=ViewTaskOutput(),
        )

    def run(self, params={}):
        task_id = params.get(Input.TASK_ID, "")
        endpoint = f"tasks/view/{task_id}"
        response = self.connection.api.send(endpoint)
        return {Output.TASK: response.get("task")}
