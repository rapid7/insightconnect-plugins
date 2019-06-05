import komand
from .schema import DeleteFolderInput, DeleteFolderOutput
# Custom imports below

class DeleteFolder(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_folder',
                description='Delete specific folder',
                input=DeleteFolderInput(),
                output=DeleteFolderOutput())

    def run(self, params={}):
        client = self.connection.box_connection
        try:
          client.folder(folder_id=params.get('id')).delete()
          return {"status": True}
        except:
          return {"status": False}

    def test(self):
        try:
          client = self.connection.box_connection
          return {'status': True }
        except:
          raise
