import insightconnect_plugin_runtime
from .schema import CreateCaseInput, CreateCaseOutput, Input, Output, Component

# Custom imports below
import requests
from thehive4py.models import Case, CaseTask


class CreateCase(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_case",
            description=Component.DESCRIPTION,
            input=CreateCaseInput(),
            output=CreateCaseOutput(),
        )

    def run(self, params={}):

        client = self.connection.client

        self.logger.info(f"Input: {params}")
        task = CaseTask(
            title=params.get(Input.TASK).get("title", None),
            description=params.get(Input.TASK).get("description", None),
            flag=params.get(Input.TASK).get("flag", False),
            owner=params.get(Input.TASK).get("owner", None),
            status=params.get(Input.TASK).get("status", None),
            startDate=params.get(Input.TASK).get("startDate", None),
        )

        case = Case(
            title=params.get(Input.TITLE, None),
            tlp=params.get(Input.TLP, 2),
            flag=params.get(Input.FLAG, False),
            tags=params.get(Input.TAGS, []),
            description=params.get(Input.DESCRIPTION, None),
            tasks=[task],
            customFields=params.get(Input.CUSTOMFIELDS, None),
        )

        try:
            new_case = client.create_case(case)
            new_case.raise_for_status()
        except requests.exceptions.HTTPError:
            self.logger.error(new_case.json())
            raise
        except:
            self.logger.error("Failed to create case")
            raise

        return {Output.CASE: new_case.json()}
