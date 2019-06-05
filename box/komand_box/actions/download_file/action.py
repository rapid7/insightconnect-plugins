import komand
from .schema import DownloadFileInput, DownloadFileOutput
# Custom imports below
import base64

class DownloadFile(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='download_file',
                description='Download file by ID',
                input=DownloadFileInput(),
                output=DownloadFileOutput())

    def run(self, params={}):
      client = self.connection.box_connection
      try:
        downloaded_file_obj = client.file(file_id=params.get('file_id'))
        url = downloaded_file_obj.get_shared_link_download_url()
        file = base64.b64encode(downloaded_file_obj.content())
        return {"status": True, "url": url, "file": str(file)}
      except:
        return {"status": False}

    def test(self):
      try:
        client = self.connection.box_connection
        return {'status': True }
      except:
        raise
