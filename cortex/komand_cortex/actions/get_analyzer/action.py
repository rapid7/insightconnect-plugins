import komand
from .schema import GetAnalyzerInput, GetAnalyzerOutput
# Custom imports below
import requests
from cortex4py.api import CortexException


class GetAnalyzer(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_analyzer',
                description='List enabled analyzers within Cortex',
                input=GetAnalyzerInput(),
                output=GetAnalyzerOutput())

    def run(self, params={}):
        """TODO: Run action"""
        client = self.connection.client
 
        _id = params.get('analyzer_id')

        if _id:
            self.logger.info('User specified Analyzer ID: %s', _id)
            url = '{}/{}/{}'.format(self.connection.url, 'api/analyzer', _id)
            try:
                out = [requests.get(url).json()]
            except:
                self.logger.error('Request failed')
                raise
        else:
            try:
                out = client.get_analyzers()
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
