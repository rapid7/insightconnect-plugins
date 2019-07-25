import komand
from .schema import CreateProjectInput, CreateProjectOutput, Input, Output, Component
from ...util import project


class CreateProject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_project',
                description=Component.DESCRIPTION,
                input=CreateProjectInput(),
                output=CreateProjectOutput())

    def run(self, params={}):
        return {
            Output.PROJECT: project.Project.create(self.connection.config, params.get(Input.NAME))
        }
