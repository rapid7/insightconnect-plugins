import komand
from .schema import GetProjectInput, GetProjectOutput, Input, Output, Component
from ...util import project


class GetProject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_project',
                description=Component.DESCRIPTION,
                input=GetProjectInput(),
                output=GetProjectOutput())

    def run(self, params={}):
        return {
            Output.PROJECT: project.Project.get(self.connection.config, params.get(Input.NAME))
        }
