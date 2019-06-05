import komand
from .schema import ClaimInput, ClaimOutput
# Custom imports below
from komand_phabricator.util.editor import ManiphesEdit
from komand_phabricator.util.editor import TestAction


class Claim(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='claim',
                description='Claim a task',
                input=ClaimInput(),
                output=ClaimOutput())

    def run(self, params={}):

        if not self.connection.phab:
            self.logger.error("Claim: Run: Empty Phabricator object")
            raise Exception("Claim: Run: Empty Phabricator object")

        id = params.get('id',None)

        searchedUser = self.connection.phab.user.whoami()

        if not searchedUser:
            self.logger.error("Claim: Run: Can't find user")
            raise Exception("Claim: Run: Can't find user")

        foundUserPhid = searchedUser.phid

        maniphest = ManiphesEdit(self.connection.phab, action=self, objectIdentifier=id)
        try:
            id = maniphest.edit([{"type": "owner", "value": foundUserPhid},])
        except Exception as e:
            self.logger.error("Claim: Run: Problem with request".format(e.errno, e.strerror))
            raise e

        if id is None:
            self.logger.error("Claim: Run: Can't assign user")
            raise Exception("Claim: Run: Can't assign user")
        else:
            return {"message":"User assigned"}

    def test(self):
        test = TestAction(action=self)

        test.checkPhabIsEmpty(self.connection.phab)
        test.wrongHealthCheck(self.connection.phab)

        return {}
