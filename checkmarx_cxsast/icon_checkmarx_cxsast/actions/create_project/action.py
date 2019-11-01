import komand
from icon_checkmarx_cxsast.actions.create_project.schema import (
    CreateProjectInput,
    CreateProjectOutput,
    Component
)
# Custom imports below


class CreateProject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_project',
                description=Component.DESCRIPTION,
                input=CreateProjectInput(),
                output=CreateProjectOutput())

    def run(self, params={}):
        return self.connection.client.create_project(params)
