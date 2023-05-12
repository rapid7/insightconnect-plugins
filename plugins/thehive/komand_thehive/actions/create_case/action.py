import insightconnect_plugin_runtime
from .schema import CreateCaseInput, CreateCaseOutput, Component, Input, Output

# Custom imports below
import time


class CreateCase(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_case",
            description=Component.DESCRIPTION,
            input=CreateCaseInput(),
            output=CreateCaseOutput(),
        )

    def run(self, params={}):
        # TODO - Don't forget to fix up the custom types in spec file!!
        case = {
            "title": params.get(Input.TITLE, None),
            "description": params.get(Input.DESCRIPTION, None),
            "tlp": params.get(Input.TLP),
            "pap": params.get(Input.PAP),
            "severity": params.get(Input.SEVERITY, 2),
            "flag": params.get(Input.FLAG),
            "tags": params.get(Input.TAGS, []),
            "startDate": params.get(Input.STARTDATE, int(time.time()) * 1000),
            "template": params.get(Input.TEMPLATE, None),
            "owner": params.get(Input.OWNER, ""),
            "metrics": params.get(Input.METRICS, {}),
            "customFields": params.get(Input.CUSTOMFIELDS, None),
            "tasks": params.get(Input.TASKS, None),
            "summary": params.get(Input.SUMMARY, ""),
        }

        self.logger.info(f"Input: {case}")
        response = self.connection.client.create_case(case=case)

        return {Output.CASE: response}
