import komand
from .schema import CreatetaskInput, CreatetaskOutput
# Custom imports below
from komand_phabricator.util.editor import ManiphesEdit
from komand_phabricator.util.editor import TestAction


class Createtask(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='createtask',
                description='Create a new task',
                input=CreatetaskInput(),
                output=CreatetaskOutput())

    def run(self, params={}):
        phid = ""

        if not self.connection.phab:
            self.logger.error("Createtask: Run: Empty Phabricator object")
            raise Exception("Createtask: Run: Empty Phabricator object")

        title = params.get('title',None)
        description = params.get('description',None)

        if not description:
            self.logger.info("Empty description")
            description = ""

        maniphest = ManiphesEdit(self.connection.phab, action=self)
        try:
            id = maniphest.edit([{"type": "title", "value": title}, {"type": "description", "value": description}])
        except Exception as e:
            self.logger.error("Createtask: Run: Problem with request".format(e.errno, e.strerror))
            raise Exception("Createtask: Run: Problem with request".format(e.errno, e.strerror))

        if id is None:
            self.logger.error("Createtask: Run: Error with endpoint")
            raise Exception("Createtask: Run: Error with endpoint")
        else:
            return {"id": id}

    def test(self):
        test = TestAction()

        test.checkPhabIsEmpty(self.connection.phab)
        test.wrongHealthCheck(self.connection.phab)

        return {}
