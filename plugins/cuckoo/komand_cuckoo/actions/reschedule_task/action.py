import insightconnect_plugin_runtime
from .schema import RescheduleTaskInput, RescheduleTaskOutput, Input, Component, Output


class RescheduleTask(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="reschedule_task",
            description=Component.DESCRIPTION,
            input=RescheduleTaskInput(),
            output=RescheduleTaskOutput(),
        )

    def run(self, params={}):
        task_id = params.get(Input.TASK_ID, "")
        priority = params.get(Input.PRIORITY, "")
        if priority:
            endpoint = f"tasks/reschedule/{task_id}/{priority}"
        else:
            endpoint = f"tasks/reschedule/{task_id}"
        response = self.connection.api.send(endpoint)
        return {Output.TASK_ID: response.get("task_id"), Output.STATUS: response.get("status", "")}
