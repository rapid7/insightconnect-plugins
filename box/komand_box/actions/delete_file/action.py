import komand
from .schema import DeleteFileInput, DeleteFileOutput
# Custom imports below

class DeleteFile(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_file',
                description='Delete specific file',
                input=DeleteFileInput(),
                output=DeleteFileOutput())

    def run(self, params={}):
        client = self.connection.box_connection
        try:
          client.file(file_id=params.get('id')).delete()
          return {"status": True}
        except:
          return {"status": False}

    def test(self):
        try:
          client = self.connection.box_connection
          return {'status': True }
        except:
          raise
