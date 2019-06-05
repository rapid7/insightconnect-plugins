import komand
from .schema import GetSampleInput, GetSampleOutput
# Custom imports below
import base64


class GetSample(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_sample',
                description='Query for a sample file',
                input=GetSampleInput(),
                output=GetSampleOutput())

    def run(self, params={}):
        """TODO: Run action"""
        client = self.connection.client
        out = base64.b64encode(client.get_sample(params.get('hash'))).decode()
        return { 'file': out }

    def test(self):
        """TODO: Test action"""
        client = self.connection.client
        return { 'file': 'test' }
