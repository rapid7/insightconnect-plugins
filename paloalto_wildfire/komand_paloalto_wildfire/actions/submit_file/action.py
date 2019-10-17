import komand
from .schema import SubmitFileInput, SubmitFileOutput
# Custom imports below
import base64
import io
import pyldfire
from komand.exceptions import PluginException


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

        out = {}
        try:
            if filename:
                self.logger.info('Filename specified: %s', filename)
                out = client.submit_file(_file, filename)
            else:
                out = client.submit_file(_file)
            out['supported_file_type'] = True
        except pyldfire.WildFireException as e:
            if e.args and "Unsupport File type" in e.args[0]:  # Yes, that's the error, not a typo
                out['supported_file_type'] = False
            else:
                raise PluginException(PluginException.Preset.UNKNOWN) from e

        if 'filename' not in out.keys():
            out['filename'] = 'Unknown'

        if 'url' not in out.keys():
            out['url'] = 'Unknown'

        return {'submission': komand.helper.clean(out)}

    def test(self):
        """TODO: Test action"""
        client = self.connection.client
        return {'submission': {'filetype': 'Test', 'filename': 'Test', 'sha256': 'Test', 'md5': 'Test', 'size': 'Test'}}
