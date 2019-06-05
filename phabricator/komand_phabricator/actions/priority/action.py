import komand
from .schema import PriorityInput, PriorityOutput
# Custom imports below
from komand_phabricator.util.editor import ManiphesEdit
from komand_phabricator.util.editor import TestAction


class Priority(komand.Action):
    validPriorites = ["unbreak", "triage", "high", "normal", "low", "wish"]

    def __init__(self):
        super(self.__class__, self).__init__(
                name='priority',
                description='Change the priority of a task',
                input=PriorityInput(),
                output=PriorityOutput())

    def run(self, params={}):

        if not self.connection.phab:
            self.logger.error("Priority: Run: Empty Phabricator object")
            raise Exception("Priority: Run: Empty Phabricator object")

        id = params.get('id', None)
        priority = params.get('priority', None)

        if not priority in self.validPriorites:
            self.logger.error("Priority: Run: Task priority '{0}' is not a valid task priority. Use a priority keyword to choose a task priority: {1}".format(priority, self.validPriorites))
            raise Exception("Priority: Run: Task priority '{0}' is not a valid task priority. Use a priority keyword to choose a task priority: {1}".format(priority, self.validPriorites))

        maniphest = ManiphesEdit(self.connection.phab, action=self, objectIdentifier=id)
        try:
            id = maniphest.edit([{"type": "priority", "value": priority},])
        except Exception as e:
            self.logger.error("Priority: Run: Problem with request".format(e.errno, e.strerror))
            raise e

        if id is None:
            self.logger.error("Priority: Run: Can't change priority")
            raise Exception("Priority: Run: Can't change priority")
        else:
            return {"message":"Priority changed"}

    def test(self):
        test = TestAction()

        test.checkPhabIsEmpty(self.connection.phab)
        test.wrongHealthCheck(self.connection.phab)

        return {}
