import komand
from .schema import LockFileInput, LockFileOutput
# Custom imports below

class LockFile(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='lock_file',
                description='Lock file',
                input=LockFileInput(),
                output=LockFileOutput())

    def run(self, params={}):
        client = self.connection.box_connection
        try:
          lock = client.file(file_id=params.get('file_id')).lock(
                                  prevent_download=params.get('download_prevented'))
          return {"status": True}
        except:
          return {"status": False}

    def test(self):
        try:
          client = self.connection.box_connection
          return {'status': True }
        except:
          raise
