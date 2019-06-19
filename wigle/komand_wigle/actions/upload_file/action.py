import komand
from .schema import UploadFileInput, UploadFileOutput
# Custom imports below
import base64


class UploadFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='upload_file',
                description='Transmit a file for processing and incorporation into the database',
                input=UploadFileInput(),
                output=UploadFileOutput())

    def run(self, params={}):
        self.logger.info('UploadFile: Uploading file ...')

        file_ = params.get('file', None)
        donate = params.get('donate', False)

        file_bytes = base64.b64decode(file_['content'])
        response = self.connection.call_api(
            'post', 'file/upload', files={
                'file': (file_['filename'], file_bytes), 'donate': donate
            }
        )
        self.logger.info(response)
        return response

    def test(self):
        return {
          "results": {
            "timeTaken": "0",
            "filesize": 6,
            "filename": "1535480859_FILE",
            "transids": [
              {
                "file": "1535480859_FILE",
                "size": 6,
                "transId": "20180828-00527"
              }
            ]
          },
          "observer": "anonymous"
        }
