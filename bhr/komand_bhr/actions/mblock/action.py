import komand
from .schema import MblockInput, MblockOutput


class Mblock(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='mblock',
                description='Send a batch block request',
                input=MblockInput(),
                output=MblockOutput())

    def run(self, params={}):
        batch  = params.get('batch')
        if type(batch) is not list:
          raise Exception('Run: List of dictionaries required: [ { "cidr": "1.1.1.1", .. }, { "cidr": "1.1.1.1", .. ]')
        client = self.connection.client
        result = client.mblock(batch)
        return { 'result': result }

    def test(self):
        """TODO: Test action"""
        return {}
