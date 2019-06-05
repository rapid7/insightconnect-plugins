import komand
from .schema import UnsubscribeInput, UnsubscribeOutput
# Custom imports below
from komand_phabricator.util.editor import ManiphesEdit
from komand_phabricator.util.editor import TestAction


class Unsubscribe(komand.Action):

    foundedSubscribes = []

    def __init__(self):
        super(self.__class__, self).__init__(
                name='unsubscribe',
                description='Remove yourself as a subscriber',
                input=UnsubscribeInput(),
                output=UnsubscribeOutput())

    def run(self, params={}):

        if not self.connection.phab:
            self.logger.error("Unsubscribe: Run: Empty Phabricator object")
            raise Exception("Unsubscribe: Run: Empty Phabricator object")

        id = params.get('id',None)

        searchedUser = self.connection.phab.user.whoami()

        if not searchedUser:
            self.logger.error("Unsubscribe: Run: Can't find user")
            raise Exception("Unsubscribe: Run: Can't find user")

        foundUserPhid = searchedUser.phid
        self.logger.info("Unsubscribe: Run: Founded user {0}".format(foundUserPhid))

        maniphest = ManiphesEdit(self.connection.phab, action=self, objectIdentifier=id)
        try:
            id = maniphest.edit([{"type": "subscribers.remove", "value": [foundUserPhid,]},])
        except Exception as e:
            self.logger.error("Unsubscribe: Run: Problem with request".format(e.errno, e.strerror))
            raise Exception("Unsubscribe: Run: Problem with request".format(e.errno, e.strerror))

        if id is None:
            self.logger.error("Unsubscribe: Run: Problem with adding projects and users {0} to subscribers".format(self.foundedSubscribes))
            raise Exception("Unsubscribe: Run: Problem with adding projects and users {0} to subscribers".format(self.foundedSubscribes))

        return {"message":"Removed"}

    def getSubscribesFromPHID(self, subscribes, name):
        elements = []
        for subscribe in subscribes:
            if name in subscribe:
                elements.append(subscribe)
        return elements

    def addToFounded(self, elements):
        if elements:
            founded = self.connection.phab.project.search(constraints={"phids": elements})
            if founded.data:
                for found in founded.data:
                    self.foundedSubscribes.append(found["phid"])

    def test(self):
        test = TestAction()

        test.checkPhabIsEmpty(self.connection.phab)
        test.wrongHealthCheck(self.connection.phab)

        return {}
