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

        json_task_data = params.get(Input.JSON)

        if json_task_data:
            task = json_task_data
        else:
            task = {
                "id": params.get(Input.ID),
                "title": params.get(Input.TITLE),
                "description": params.get(Input.DESCRIPTION),
                "status": params.get(Input.STATUS),
                "flag": params.get(Input.FLAG),
                "startDate": params.get(Input.STARTDATE, int(time.time()) * 1000),
                "owner": params.get(Input.OWNER)
            }

        self.logger.info(f"Input: {task}")
        
        response = self.connection.client.create_task_in_case(task=task)

        return {Output.CASE: response}
        # client = self.connection.client
        #
        # self.logger.info(params)
        # task = CaseTask(
        #     title=params.get("task").get("title", None),
        #     description=params.get("task").get("description", None),
        #     flag=params.get("task").get("flag", False),
        #     owner=params.get("task").get("owner", None),
        #     status=params.get("task").get("status", None),
        # )
        #
        # try:
        #     task = client.create_case_task(params.get("id"), task)
        #     task.raise_for_status()
        # except requests.exceptions.HTTPError:
        #     self.logger.error(task.json())
        #     raise
        # except:
        #     self.logger.error("Failed to create task")
        #     raise
        #
        # d = task.json()
        # # If API returns None, manually do what the library does elsewhere
        # # https://github.com/CERT-BDF/TheHive4py/blob/master/thehive4py/models.py#L44
        # if "startDate" in d:
        #     if isinstance(d["startDate"], type(None)):
        #         d["startDate"] = int(time.time()) * 1000
        #
        # return {"case": d}
