import komand
from .schema import ListAvailableProjectsInput, ListAvailableProjectsOutput, Input, Output, Component
from ...util import project


class ListAvailableProjects(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_available_projects',
                description=Component.DESCRIPTION,
                input=ListAvailableProjectsInput(),
                output=ListAvailableProjectsOutput())

    def run(self, params={}):
        return {
            Output.PROJECTS: project.Project.all(self.connection.config)
        }
