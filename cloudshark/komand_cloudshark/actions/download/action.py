import komand
from .schema import DownloadInput, DownloadOutput
# Custom imports below
import urllib2


class Download(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='download',
                description='Download capture file',
                input=DownloadInput(),
                output=DownloadOutput())

    def run(self, params={}):
        base = self.connection.base
        token = self.connection.token
        url = base + token + '/download/' + params.get('cid')
        resp = urllib2.urlopen(url)
        capture_file = komand.helper.encode_string(resp.read())
        return { 'capture_file': capture_file, 'status': resp.code }

    def test(self):
        """TODO: Test action"""
        return {}
