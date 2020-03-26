import komand
from .schema import AssessmentsInput, AssessmentsOutput, Component, Output


class Assessments(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='assessments',
            description=Component.DESCRIPTION,
            input=AssessmentsInput(),
            output=AssessmentsOutput())

    def run(self, params={}):
        return {
            Output.DATA: self.connection.attackerKB_api.call_api_pages(f"assessments", params=params)
        }
