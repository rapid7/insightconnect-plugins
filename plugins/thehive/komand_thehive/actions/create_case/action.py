import insightconnect_plugin_runtime
from .schema import CreateCaseInput, CreateCaseOutput, Component, Input, Output

# Custom imports below
import datetime


class CreateCase(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_case",
            description=Component.DESCRIPTION,
            input=CreateCaseInput(),
            output=CreateCaseOutput(),
        )

    def run(self, params={}):

        case = {
            "title": params.get(Input.TITLE),
            "description": params.get(Input.DESCRIPTION),
            "severity": params.get(Input.SEVERITY),
            "startDate": params.get(Input.STARTDATE, datetime.datetime.now()),
            "endDate": params.get(Input.ENDDATE),
            "tags": params.get(Input.TAGS, None),
            "flag": params.get(Input.FLAG),
            "tlp": params.get(Input.TLP),
            "pap": params.get(Input.PAP),
            "status": params.get(Input.STATUS),
            "summary": params.get(Input.SUMMARY),
            "assignee": params.get(Input.ASSIGNEE),
            "customFields": params.get(Input.CUSTOMFIELDS),
            "caseTemplate": params.get(Input.CASETEMPLATE, None),
            "tasks": params.get(Input.TASKS, None),
            "sharingParameters": params.get(Input.SHARINGPARAMETERS, []),
            "taskRule": params.get(Input.TASKRULE, None),
            "observableRule": params.get(Input.OBSERVABLERULE, None),
        }

        self.logger.info(f"Input: {case}")

        response = self.connection.client.create_case(case=case)

        return {Output.CASE: response.json()}
        #
        # client = self.connection.client
        #
        # self.logger.info("Input: %s", params)
        # task = CaseTask(
        #     title=params.get("task").get("title", None),
        #     description=params.get("task").get("description", None),
        #     flag=params.get("task").get("flag", False),
        #     owner=params.get("task").get("owner", None),
        #     status=params.get("task").get("status", None),
        #     startDate=params.get("task").get("startDate", None),
        # )
        #
        # case = Case(
        #     title=params.get("title", None),
        #     tlp=params.get("tlp", 2),
        #     flag=params.get("flag", False),
        #     tags=params.get("tags", []),
        #     description=params.get("description", None),
        #     tasks=[task],
        #     customFields=params.get("customFields", None),
        # )
        #
        # try:
        #     new_case = client.create_case(case)
        #     new_case.raise_for_status()
        # except requests.exceptions.HTTPError:
        #     self.logger.error(new_case.json())
        #     raise
        # except:
        #     self.logger.error("Failed to create case")
        #     raise
        #
        # return {"case": new_case.json()}
