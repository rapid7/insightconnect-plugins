import komand
from .schema import GetFolderInput, GetFolderOutput
# Custom imports below

class GetFolder(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_folder',
                description='Retrieve specific folder ID',
                input=GetFolderInput(),
                output=GetFolderOutput())

    def run(self, params={}):
        client = self.connection.box_connection
        try:
            response = client.search(params.get('folder_name'), limit=2, offset=0)
            for folder in response:
                return {"id": folder.id}
        except:
            self.logger.error('Error occured')
            return {}

    def test(self):
        try:
            client = self.connection.box_connection
            return {'status': True }
        except:
            raise
