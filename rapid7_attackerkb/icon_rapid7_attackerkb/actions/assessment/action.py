import komand
from .schema import AssessmentInput, AssessmentOutput, Input, Component
from komand.exceptions import PluginException


class Assessment(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='assessment',
            description=Component.DESCRIPTION,
            input=AssessmentInput(),
            output=AssessmentOutput())

    def run(self, params={}):
        if not params.get(Input.ID):
            raise PluginException(cause="Input error",
                                  assistance="ID can't be empty")

        return self.connection.attackerKB_api.call_api(f"assessments/{params.get(Input.ID)}")
