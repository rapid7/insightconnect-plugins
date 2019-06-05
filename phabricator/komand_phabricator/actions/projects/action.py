import komand
from .schema import ProjectsInput, ProjectsOutput
# Custom imports below
from komand_phabricator.util.editor import ManiphesEdit
from komand_phabricator.util.editor import TestAction


class Projects(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='projects',
                description='Add related projects to a task',
                input=ProjectsInput(),
                output=ProjectsOutput())

    def run(self, params={}):

        if not self.connection.phab:
            self.logger.error("Projects: Run: Empty Phabricator object")
            raise Exception("Projects: Run: Empty Phabricator object")

        id = params.get('id',None)
        projects = params.get('projects',None)

        foundedProjects = []
        for project in projects:
            searchedProject = self.connection.phab.project.search(constraints={"name": project})
            if searchedProject.data:
                foundedProjects.append(searchedProject.data[0]["phid"])

        maniphest = ManiphesEdit(self.connection.phab, action=self, objectIdentifier=id)
        try:
            id = maniphest.edit([{"type": "subscribers.add", "value": foundedProjects},])
        except Exception as e:
            self.logger.error("Projects: Run: Problem with request".format(e.errno, e.strerror))
            raise e

        if id is None:
            self.logger.error("Projects: Run: Problem with adding projects {0} to subscribers".format(foundedProjects))
            raise Exception("Projects: Run: Problem with adding projects {0} to subscribers".format(foundedProjects))

        return {"message":"Projects added"}

    def test(self):
        test = TestAction()

        test.checkPhabIsEmpty(self.connection.phab)
        test.wrongHealthCheck(self.connection.phab)

        return {}
