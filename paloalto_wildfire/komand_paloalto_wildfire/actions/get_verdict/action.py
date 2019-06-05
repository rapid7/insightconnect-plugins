import komand
from .schema import GetVerdictInput, GetVerdictOutput
# Custom imports below


class GetVerdict(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_verdict',
                description='Query for a files classification',
                input=GetVerdictInput(),
                output=GetVerdictOutput())

    def run(self, params={}):
        """TODO: Run action"""
        client = self.connection.client
        out = client.get_verdicts(params.get('hash'))

        return { 'verdict': out }

    def test(self):
        """TODO: Test action"""
        client = self.connection.client
        return { 'verdict': 'Not found' }
