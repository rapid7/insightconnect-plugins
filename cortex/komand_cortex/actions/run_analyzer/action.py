import komand
from .schema import RunAnalyzerInput, RunAnalyzerOutput
# Custom imports below
from cortex4py.api import CortexException


class RunAnalyzer(komand.Action):
    tlp = { 
        "WHITE": 0,
        "GREEN": 1,
        "AMBER": 2,
        "RED": 3
    }

    def __init__(self):
        super(self.__class__, self).__init__(
                name='run_analyzer',
                description='Run analyzers on an observable',
                input=RunAnalyzerInput(),
                output=RunAnalyzerOutput())

    def run(self, params={}):
        """TODO: Run action"""
        client = self.connection.client
        _id = params.get('analyzer_id')
        observable = params.get('observable')
        data_type = params.get('attributes').get('dataType')
        tlp_num = params.get('attributes').get('tlp')
        #tlp_num = tlp[params.get('attributes').get('tlp')]

        if not _id:
            self.logger.error('Analyzer ID not provided')
            raise Exception('Missing Analyzer ID')

        for k,v in self.tlp.items():
            if self.tlp[k] == tlp_num:
                self.logger.info('TLP: %s is %s', tlp_num, k)
                break

        try:
            out = client.run_analyzer(_id, data_type, tlp_num, observable)
        except CortexException:
            self.logger.error('Failed to run analyzer')
            raise

        # Make sure report key doesn't exist to avoid updating job type in spec (lazy)
        # and it always seems to have a value of None and the report can be obtained through
        # the Get Job Report action anyway (so maybe smart?)
        try:
            del out['report']
        except KeyError:
            pass

        return out

    def test(self):
        """TODO: Test action"""
        client = self.connection.client

        try:
            out = client.get_analyzers()
        except CortexException:
            self.logger.error('Failed to test getting analyzers')
            raise

        return {  
            'status': 'Success',
            'date': 1,
            'id': 'Test',
            'status': 'Success',
            'artifact': {},
            'analyzerId': 'Test'
        }
