import komand
from .. import demo_test
from .schema import LookupHashInput, LookupHashOutput


class LookupHash(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='lookup_hash',
                description='This action is used to retrieve information about a specified hash',
                input=LookupHashInput(),
                output=LookupHashOutput())

    def run(self, params={}):
        try:
            hash_ID = params.get("hash")
            hash_report = self.connection.client.lookup_hash(hash_ID)
            return hash_report
        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        return demo_test.demo_test(self.connection.token, self.logger)
