import komand
from .schema import SubmitFileInput, SubmitFileOutput
# Custom imports below
import base64
import io


class SubmitFile(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit_file',
                description='Submit a file for analysis',
                input=SubmitFileInput(),
                output=SubmitFileOutput())

    def run(self, params={}):
        """TODO: Run action"""
        client = self.connection.client
        _file = io.BytesIO(base64.b64decode(params.get('file')))
        filename = params.get('filename')

        if filename:
            self.logger.info('Filename specified: %s', filename)
            out = client.submit_file(_file, filename)
        else:
            out = client.submit_file(_file)
            
        if not out['filename']:
            out['filename'] = 'Unknown'

        if not out['url']:
            out['url'] = 'Unknown'

        return { 'submission': dict(out) }

    def test(self):
        """TODO: Test action"""
        client = self.connection.client
        return { 'submission': { 'filetype': 'Test', 'filename': 'Test', 'sha256': 'Test', 'md5': 'Test', 'size': 'Test' } }
