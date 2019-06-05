import komand
from .schema import DownloadInput, DownloadOutput
# Custom imports below
import os
import base64
import ftputil


class Download(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='download',
                description='Download file from server',
                input=DownloadInput(),
                output=DownloadOutput())

    def run(self, params={}):
        pathval = params.get('path')
        local_filename = os.path.basename(pathval)
        # Actually download file
        try:
            self.connection.ftp_host.download(pathval, local_filename)
        except (ftputil.error.FTPIOError, ftputil.error.PermanentError, ftputil.error.FTPError) as e:
            if type(e) is ftputil.error.FTPIOError:
              self.logger.error(e)
            elif type(e) is ftputil.error.PermanentError:
              self.logger.error(e)
            else:
              self.logger.error('%s: %s', e.errno, e.stderror)
            return { 'downloaded': False }
        # Encode file as base64
        with open(local_filename, 'rb') as f:
            encoded = base64.b64encode(f.read()).decode('utf-8')
            return { 'downloaded': True, 'download': encoded}

    def test(self):
        """TODO: Test action"""
        return {}
