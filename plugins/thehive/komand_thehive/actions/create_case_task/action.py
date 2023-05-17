import insightconnect_plugin_runtime
from .schema import CreateCaseTaskInput, CreateCaseTaskOutput, Component, Input, Output

# Custom imports below
import time


class CreateCaseTask(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_case_task",
            description=Component.DESCRIPTION,
            input=CreateCaseTaskInput(),
            output=CreateCaseTaskOutput(),
        )

    def run(self, params={}):

        case_id = params.get(Input.ID)
        json_task_data = params.get(Input.JSONDATA)

        if json_task_data:
            task = json_task_data
        else:
            task = {
                "title": params.get(Input.TITLE),
                "description": params.get(Input.DESCRIPTION),
                "status": params.get(Input.STATUS),
                "flag": params.get(Input.FLAG),
                "startDate": params.get(Input.STARTDATE, int(time.time()) * 1000),
                "owner": params.get(Input.OWNER),
            }

        self.logger.info(f"Input: {task}")

        response = self.connection.client.create_task_in_case(case_id=case_id, task=task)

        return {Output.CASE: response}
