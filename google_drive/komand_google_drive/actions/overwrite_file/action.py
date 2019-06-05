import komand
from .schema import OverwriteFileInput, OverwriteFileOutput
# Custom imports below
from io import BytesIO
from base64 import b64decode
from googleapiclient.http import MediaIoBaseUpload
from apiclient import errors


class OverwriteFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='overwrite_file',
                description='Overwrites a file with new data',
                input=OverwriteFileInput(),
                output=OverwriteFileOutput())

    def run(self, params={}):
        content = params.get('content')
        file_id = params.get('file_id')
        new_file_name = params.get('new_file_name')
        new_mime_type = params.get('new_mime_type')

        file_bytes = BytesIO(b64decode(content))

        # Apply mime_type.
        mime_type = None
        if new_mime_type == 'Docs':
            mime_type = 'application/vnd.google-apps.document'
        if new_mime_type == 'Sheets':
            mime_type = 'application/vnd.google-apps.spreadsheet'
        if new_mime_type == 'Slides':
            mime_type = 'application/vnd.google-apps.presentation'

        try:

            # File's new content.
            media = MediaIoBaseUpload(file_bytes, mime_type, resumable=True)

            # Send the request to the API.
            if new_file_name:
                updated_file = self.connection.service.files().update(
                    body={'name': new_file_name, 'mimeType': mime_type},
                    fileId=file_id,
                    media_mime_type=mime_type,
                    media_body=media).execute()
            else:
                updated_file = self.connection.service.files().update(
                    body={'mimeType': mime_type},
                    fileId=file_id,
                    media_mime_type=mime_type,
                    media_body=media).execute()

            file_id = updated_file['id']

            return {'file_id': file_id}
        except errors.HttpError as error:
            self.logger.error('An error occurred: %s' % error)
            raise
        except:
            self.logger.error('An unexpected error occurred')
            raise

    def test(self):
        # TODO: Implement test function
        return {}
