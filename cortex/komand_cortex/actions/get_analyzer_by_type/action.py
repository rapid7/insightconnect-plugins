import komand
from .schema import GetAnalyzerByTypeInput, GetAnalyzerByTypeOutput
# Custom imports below
from cortex4py.api import CortexException


class GetAnalyzerByType(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_analyzer_by_type',
                description='List analyzers that can act upon a given datatype',
                input=GetAnalyzerByTypeInput(),
                output=GetAnalyzerByTypeOutput())

    def run(self, params={}):
        """TODO: Run action"""
        client = self.connection.client

        try:
            out = client.get_analyzers(data_type=params.get('type'))
        except CortexException:
            self.logger.error('Failed to get analyzers')
            raise

        return { 'list': out }

    def test(self):
        """TODO: Test action"""
        client = self.connection.client

        try:
            out = client.get_analyzers()
        except CortexException:
            self.logger.error('Failed to test getting analyzers')
            raise

        return { 'list': out }
