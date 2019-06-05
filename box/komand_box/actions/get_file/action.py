import komand
from .schema import GetFileOutput, GetFileInput
# Custom imports below


class GetFile(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_file',
                description='Retrieve specific file ID',
                input=GetFileInput(),
                output=GetFileOutput())

    def run(self, params={}):
        client = self.connection.box_connection
        try:
          response = client.search(params.get('file_name'), limit=2, offset=0)
          for file in response:
            return {"id": file.id}
        except:
          self.logger.error('Error occured')
        return {}

    def test(self):
        try:
          client = self.connection.box_connection
          return {'status': True }
        except:
          raise
