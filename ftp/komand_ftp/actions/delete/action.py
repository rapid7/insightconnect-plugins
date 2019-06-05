import komand
from .schema import DeleteInput, DeleteOutput
# Custom imports below
import ftputil


class Delete(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete',
                description='Delete file from server',
                input=DeleteInput(),
                output=DeleteOutput())

    def run(self, params={}):
        pathval = params.get('path')
        try:
            self.connection.ftp_host.remove(pathval)
        except (ftputil.error.FTPIOError, ftputil.error.PermanentError, ftputil.error.FTPError) as e:
            if type(e) is ftputil.error.FTPIOError:
              self.logger.error(e)
            elif type(e) is ftputil.error.PermanentError:
              self.logger.error(e)
            else:
              self.logger.error('%s: %s', e.errno, e.stderror)
            return { 'deleted': False }
        return { 'deleted': True }

    def test(self):
        """TODO: Test action"""
        return {}
