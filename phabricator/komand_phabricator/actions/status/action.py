import komand
from .schema import StatusInput, StatusOutput
# Custom imports below
from komand_phabricator.util.editor import ManiphesEdit
from komand_phabricator.util.editor import TestAction


class Status(komand.Action):
    validStatuses = ["open","resolved","wontfix","invalid","spite"]

    def __init__(self):
        super(self.__class__, self).__init__(
                name='status',
                description='Change the status of a task',
                input=StatusInput(),
                output=StatusOutput())

    def run(self, params={}):

        if not self.connection.phab:
            self.logger.error("Status: Run: Empty Phabricator object")
            raise Exception("Status: Run: Empty Phabricator object")

        id = params.get('id', None)
        status = params.get('status', None)

        if not status in self.validStatuses:
            self.logger.error("Status: Run: You must set valid status {0}".format(self.validStatuses))
            raise Exception("Status: Run: You must set valid status {0}".format(self.validStatuses))

        maniphest = ManiphesEdit(self.connection.phab,action=self, objectIdentifier=id)
        try:
            id = maniphest.edit([{"type": "status", "value": status},])
        except Exception as e:
            self.logger.error("Status: Run: Problem with request".format(e.errno, e.strerror))
            raise e

        if id is None:
            self.logger.error("Status: Run: Can't set status")
            raise Exception("Status: Run: Can't set status")
        else:
            return {"message":"Status changed"}

    def test(self):
        test = TestAction()

        test.checkPhabIsEmpty(self.connection.phab)
        test.wrongHealthCheck(self.connection.phab)

        return {}
