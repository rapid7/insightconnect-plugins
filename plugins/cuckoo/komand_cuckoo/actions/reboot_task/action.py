import insightconnect_plugin_runtime
from .schema import RebootTaskInput, RebootTaskOutput, Input, Component


class RebootTask(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="reboot_task",
            description=Component.DESCRIPTION,
            input=RebootTaskInput(),
            output=RebootTaskOutput(),
        )

    def run(self, params={}):
        task_id = params.get(Input.TASK_ID, "")
        endpoint = f"tasks/reboot/{task_id}"
        response = self.connection.api.send(endpoint)
        return response
