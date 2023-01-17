import insightconnect_plugin_runtime
from .schema import CreateTaskInput, CreateTaskOutput, Input, Output, Component

# Custom imports below
from icon_bmc_helix_itsm.util.constants import TaskRequest


class CreateTask(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="createTask", description=Component.DESCRIPTION, input=CreateTaskInput(), output=CreateTaskOutput()
        )

    def run(self, params={}):
        task_parameters = {
            TaskRequest.SUMMARY: params.get(Input.SUMMARY),
            TaskRequest.ROOT_REQUEST_MODE: "Real",
            TaskRequest.NOTES: params.get(Input.NOTES),
            TaskRequest.TASK_TYPE: "Manual",
            TaskRequest.TASK_NAME: params.get(Input.TASKNAME),
            TaskRequest.PRIORITY: params.get(Input.PRIORITY),
            TaskRequest.LOCATION_COMPANY: params.get(Input.LOCATIONCOMPANY),
            TaskRequest.ROOT_REQUEST_FORM_NAME: "HPD:Help Desk",
        }
        return {
            Output.TASKID: self.connection.api_client.create_task(params.get(Input.INCIDENTNUMBER), task_parameters)
        }
