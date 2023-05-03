import komand
from .schema import GetCaseInput, GetCaseOutput, Input, Output, Component

# Custom imports below


class GetCase(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_case",
            description=Component.DESCRIPTION,
            input=GetCaseInput(),
            output=GetCaseOutput(),
        )

    def run(self, params={}):
        case_id = params.get(Input.ID)
        result = self.connection.client.get_case(case_id)
        return {Output.CASE: result.json()}
        # try:
        #     case = client.get_case(params.get("id"))
        #     case.raise_for_status()
        # except requests.exceptions.HTTPError:
        #     self.logger.error(case.json())
        #     raise
        # except:
        #     self.logger.error("Failed to get case")
        #     raise
        #
        # return {"case": case.json()}
