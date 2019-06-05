import komand
from .schema import SubscribeOutput, SubscribeInput
# Custom imports below
from komand_phabricator.util.editor import ManiphesEdit
from komand_phabricator.util.editor import TestAction


class Subscribe(komand.Action):
    foundedSubscribes = []

    def __init__(self):
        super(self.__class__, self).__init__(
                name='subscribe',
                description='Add users or projects as subscribers',
                input=SubscribeInput(),
                output=SubscribeOutput())

    def run(self, params={}):

        if not self.connection.phab:
            self.logger.error("Subscribe: Run: Empty Phabricator object")
            raise Exception("Subscribe: Run: Empty Phabricator object")

        id = params.get('id',None)
        subscribes = params.get('subscribes', None)

        users = self.getSubscribesFromPHID(subscribes, "USER")
        projects = self.getSubscribesFromPHID(subscribes, "PROJ")

        self.addToFounded(users)
        self.addToFounded(projects)

        if not self.foundedSubscribes:
            self.logger.error("Subscribe: Run: Nothing to do")
            raise Exception("Subscribe: Run: Nothing to do")

        maniphest = ManiphesEdit(self.connection.phab, action=self, objectIdentifier=id)
        try:
            id = maniphest.edit([{"type": "subscribers.add", "value": self.foundedSubscribes},])
        except Exception as e:
            self.logger.error("Subscribe: Run: Problem with request".format(e.errno, e.strerror))
            raise e

        if id is None:
            self.logger.error("Subscribe: Run: Problem with adding projects and users {0} to subscribers".format(founded))
            raise Exception("Subscribe: Run: Problem with adding projects and users {0} to subscribers".format(founded))

        return {"message":"Subscribes added"}

    def getSubscribesFromPHID(self, subscribes, name):
        elements = []
        for subscribe in subscribes:
            if name in subscribe:
                elements.append(subscribe)
        return elements

    def addToFounded(self, founded):
        if founded:
            for found in founded:
                self.foundedSubscribes.append(found)

    def test(self):
        test = TestAction()

        test.checkPhabIsEmpty(self.connection.phab)
        test.wrongHealthCheck(self.connection.phab)

        return {}
