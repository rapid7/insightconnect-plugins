import komand
from .schema import UploadFileInput, UploadFileOutput
# Custom imports below
import io

class UploadFile(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='upload_file',
                description='Upload file to folder',
                input=UploadFileInput(),
                output=UploadFileOutput())

    def run(self, params={}):
        file_name = params.get('name')
        folder_id = params.get('folder_id')
        stream = io.StringIO()
        stream.write(params.get('file'))
        stream.seek(0)
        client = self.connection.box_connection
        file_upload = client.folder(folder_id=folder_id).upload_stream(stream, file_name)
        if file_upload.get()['id']:
          return {"status": True}
        return {"status": False}

    def test(self):
        try:
          client = self.connection.box_connection
          return {'status': True}
        except:
          raise
