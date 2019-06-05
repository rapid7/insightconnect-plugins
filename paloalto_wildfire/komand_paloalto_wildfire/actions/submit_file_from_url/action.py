import komand
from .schema import SubmitFileFromUrlInput, SubmitFileFromUrlOutput
# Custom imports below
import requests
import xmltodict


class SubmitFileFromUrl(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit_file_from_url',
                description='Submit a file for analysis via a URL',
                input=SubmitFileFromUrlInput(),
                output=SubmitFileFromUrlOutput())

    def run(self, params={}):
        """TODO: Run action"""
        endpoint =  "/publicapi/submit/url"
        client = self.connection.client
        url = 'https://{}{}'.format(self.connection.host, endpoint)

        # Formatted with None and tuples so requests sends form-data properly
        # => Send data, 299 bytes (0x12b)
        # 0000: --------------------------8557684369749613
        # 002c: Content-Disposition: form-data; name="apikey"
        # 005b:
        # 005d: 740219c8fab2606b9206b2d40626b2d1
        # 007f: --------------------------8557684369749613
        # 00ab: Content-Disposition: form-data; name="format"
        # 00d8:
        # 00da: pdf
        # 00fd: --------------------------8557684369749613--
        # ...

        req = {
            'apikey': (None, self.connection.api_key),
            'url': (None, params.get('url')),
        }

        try:
            r = requests.post(url, files=req)
            o = xmltodict.parse(r.content)
            out = dict(o['wildfire']['upload-file-info'])
        except:
            self.logger.info('Error occurred')
            raise

        if not out['filename']:
            out['filename'] = 'Unknown'

        return { 'submission': out }

    def test(self):
        """TODO: Test action"""
        client = self.connection.client
        return { 'submission': { 'filetype': 'Test', 'filename': 'Test', 'url': 'Test', 'sha256': 'Test', 'md5': 'Test', 'size': 'Test' } }
