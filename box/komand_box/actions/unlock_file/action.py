import komand
from .schema import UnlockFileInput, UnlockFileOutput
# Custom imports below

class UnlockFile(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='unlock_file',
                description='Unlock file',
                input=UnlockFileInput(),
                output=UnlockFileOutput())

    def run(self, params={}):
        client = self.connection.box_connection
        try:
          unlock = client.file(file_id=params.get('file_id')).unlock()
          return {"status": True}
        except:
          return {"status": False}

    def test(self):
        try:
          client = self.connection.box_connection
          return {'status': True }
        except:
          raise
