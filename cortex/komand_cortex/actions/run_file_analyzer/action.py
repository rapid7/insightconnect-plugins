import komand
from .schema import RunFileAnalyzerInput, RunFileAnalyzerOutput
# Custom imports below
import json
import base64
import io
import magic
import requests
from cortex4py.api import CortexException


class RunFileAnalyzer(komand.Action):
    tlp = { 
        "WHITE": 0,
        "GREEN": 1,
        "AMBER": 2,
        "RED": 3
    }

    def __init__(self):
        super(self.__class__, self).__init__(
                name='run_file_analyzer',
                description='Run analyzers on a file',
                input=RunFileAnalyzerInput(),
                output=RunFileAnalyzerOutput())


    def run(self, params={}):
        """TODO: Run action"""
        _id = params.get('analyzer_id')
        tlp_num = params.get('attributes').get('tlp')
        _file = io.BytesIO(base64.b64decode(params.get('file')))
        #tlp_num = tlp[params.get('attributes').get('tlp')]

        if params.get('attributes').get('filename'):
            filename = params.get('attributes').get('filename')
        else:
            filename = 'Not Available'

        try:
           _type = magic.Magic(mime=True).from_buffer(_file.read(1024))
           self.logger.info('MIME Content Type: %s', _type)
        except:
            self.logger.info('Unable to determine MIME Content Type of file, using %s:', _type)
            _type = 'application/octet-stream'
            pass

        # Reset file counter to beginning of file since read 1024 bytes for magic number above
        _file.seek(0)

        if not _id:
            self.logger.error('Analyzer ID not provided')
            raise Exception('Missing Analyzer ID')

        # Log TLP value
        for k,v in self.tlp.items():
            if self.tlp[k] == tlp_num:
                self.logger.info('TLP: %s is %s', tlp_num, k)
                break

        url = self.connection.url + "/api/analyzer/{}/run".format(_id)

        file_def = {
            "data": (filename, _file.read(), _type)
        }

        data = {
            "_json": json.dumps({
                "dataType": "file",
                "tlp": tlp_num
            })
        }

        try:
            out = requests.post(url, data=data, files=file_def, proxies=self.connection.proxy, verify=self.connection.verify).json()
        except Exception as e:
            self.logger.error('Failed to run file analyzer: %s', str(e))
            raise

        # Make sure report key doesn't exist to avoid updating job type in spec (lazy)
        # and it always seems to have a value of None and the report can be obtained through
        # the Get Job Report action anyway (so maybe smart?)
        try:
            del out['report']
        except TypeError:
            self.logger.error('Failed to run file analyzer: %s', out.content.decode())
            raise
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
