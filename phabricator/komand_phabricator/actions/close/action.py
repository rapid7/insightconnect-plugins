import komand
from .schema import CloseInput, CloseOutput
# Custom imports below
from komand_phabricator.util.editor import ManiphesEdit
from komand_phabricator.util.editor import TestAction


class Close(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='close',
                description='Close a task',
                input=CloseInput(),
                output=CloseOutput())

    def run(self, params={}):

        if not self.connection.phab:
            self.logger.error("Close: Run: Empty Phabricator object")
            raise Exception("Close: Run: Empty Phabricator object")

        id = params.get('id', None)

        maniphest = ManiphesEdit(self.connection.phab, action=self, objectIdentifier=id)
        try:
            id = maniphest.edit([{"type": "status", "value": "resolved"},])
        except Exception as e:
            self.logger.error("Close: Run: Problem with request".format(e.errno, e.strerror))
            raise e

        if id is None:
            self.logger.error("Close: Run: Can't close task")
            raise Exception("Close: Run: Can't close task")
        else:
            return {"message":"Task closed"}

    def test(self):
        test = TestAction()

        test.checkPhabIsEmpty(self.connection.phab)
        test.wrongHealthCheck(self.connection.phab)

        return {}
