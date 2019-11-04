import komand
from .schema import CreateBranchedProjectInput, CreateBranchedProjectOutput, Component
# Custom imports below


class CreateBranchedProject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_branched_project',
                description=Component.DESCRIPTION,
                input=CreateBranchedProjectInput(),
                output=CreateBranchedProjectOutput())

    def run(self, params={}):
        return self.connection.client.create_branched_project(
            id=params.get("id"),
            project=params.get("project"),
        )
