import komand
from .schema import AssignInput, AssignOutput
# Custom imports below
from komand_phabricator.util.editor import ManiphesEdit
from komand_phabricator.util.editor import TestAction


class Assign(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='assign',
                description='Assign specific user to task',
                input=AssignInput(),
                output=AssignOutput())

    def run(self, params={}):

        if not self.connection.phab:
            self.logger.error("Assign: Run: Empty Phabricator object")
            raise Exception("Assign: Run: Empty Phabricator object")

        id = params.get('id',None)
        user = params.get('user',None)

        searchedUser = self.connection.phab.user.search(constraints={"usernames": [user,]})

        if not searchedUser.data:
            self.logger.error("Assign: Run: Can't find user")
            raise Exception("Assign: Run: Can't find user")

        foundUserPhid = searchedUser.data[0]['phid']

        maniphest = ManiphesEdit(self.connection.phab, action=self, objectIdentifier=id)
        try:
            id = maniphest.edit([{"type": "owner", "value": foundUserPhid},])
        except Exception as e:
            self.logger.error("Assign: Run: Problem with request".format(e.errno, e.strerror))
            raise e

        if id is None:
            self.logger.error("Assign: Run: Can't assign user")
            raise Exception("Assign: Run: Can't assign user")
        else:
            return {"message":"User assigned"}

    def test(self):
        test = TestAction()

        test.checkPhabIsEmpty(self.connection.phab)
        test.wrongHealthCheck(self.connection.phab)

        return {}
