import komand
from .schema import GetFileContentsInput, GetFileContentsOutput
# Custom imports below
import googleapiclient.errors
import base64


class GetFileContents(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_file_contents',
                description='Get the contents of a file on Google Drive',
                input=GetFileContentsInput(),
                output=GetFileContentsOutput())

    def run(self, params={}):
        file_id = params.get('file_id')
        mime_type = params.get('mime_type')

        try:
            response = self.connection.service.files().export(fileId=file_id, mimeType=mime_type).execute()
        except googleapiclient.errors.HttpError as e:
            self.logger.error(e)
            raise

        _file = base64.b64encode(response)
        _file = _file.decode('UTF-8')
        return {'file': _file}

    def test(self):
        # TODO: Implement test function
        return {}
