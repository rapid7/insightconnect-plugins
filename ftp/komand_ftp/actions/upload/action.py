import komand
from .schema import UploadInput, UploadOutput
# Custom imports below
import os
import base64
import time
import ftputil


class Upload(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='upload',
                description='Upload file to server',
                input=UploadInput(),
                output=UploadOutput())

    def run(self, params={}):
        file_content = params.get('file_content')
        remote_path = params.get('remote_path')
        # Create temporary file with name based on time
        tmp_file = 'tmp' + str(time.time())
        with open(tmp_file, 'wb') as f:
            decoded = base64.b64decode(file_content)
            f.write(bytes(decoded))
        # Upload file
        try:
            self.connection.ftp_host.upload(tmp_file, remote_path)
        except (ftputil.error.FTPIOError, ftputil.error.PermanentError, ftputil.error.FTPError) as e:
            if type(e) is ftputil.error.FTPIOError:
              self.logger.error(e)
            elif type(e) is ftputil.error.PermanentError:
              self.logger.error(e)
            else:
              self.logger.error('%s: %s', e.errno, e.stderror)
            return { 'uploaded': False }

        # Clean up temporary file
        os.remove(tmp_file)    
        return { 'uploaded': True }

    def test(self):
        """TODO: Test action"""
        return {}
