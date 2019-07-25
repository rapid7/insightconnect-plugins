import komand
from .schema import GetAnalysisInput, GetAnalysisOutput, Input, Output, Component
from ...util import project


class GetAnalysis(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_analysis',
                description=Component.DESCRIPTION,
                input=GetAnalysisInput(),
                output=GetAnalysisOutput())

    def run(self, params={}):
        return {
            Output.ANALYSES: project.Project(self.connection.config, params.get(Input.PROJECT_NAME)).get_analysis(params.get(Input.ID))
        }
