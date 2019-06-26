import komand
from .schema import ListAnalysesInput, ListAnalysesOutput, Input, Output, Component
from ...util import project


class ListAnalyses(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_analyses',
                description=Component.DESCRIPTION,
                input=ListAnalysesInput(),
                output=ListAnalysesOutput())

    def run(self, params={}):
        return {
            Output.ANALYSES: project.Project(self.connection.config, params.get(Input.PROJECT_NAME)).list_analyses()
        }
